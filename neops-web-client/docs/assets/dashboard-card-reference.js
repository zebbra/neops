;(function () {
  const enhancedAttribute = 'data-neops-config-enhanced'

  function fieldSegments(path) {
    return path.split('.').filter(Boolean)
  }

  function fieldDepth(path) {
    return fieldSegments(path).length
  }

  function parentPath(path) {
    const segments = fieldSegments(path)
    segments.pop()
    return segments.join('.')
  }

  function commonPath(paths) {
    if (!paths.length) return ''
    const segments = paths.map(fieldSegments)
    const shared = []
    const shortest = Math.min(...segments.map(parts => parts.length))
    for (let index = 0; index < shortest; index += 1) {
      const segment = segments[0][index]
      if (!segments.every(parts => parts[index] === segment)) break
      shared.push(segment)
    }
    return shared.join('.')
  }

  function findParentEntry(entriesByPath, path) {
    const directParent = parentPath(path)
    return entriesByPath.get(directParent) || entriesByPath.get(directParent.replace(/\[\]$/, ''))
  }

  function localName(path) {
    return fieldSegments(path).at(-1) || path
  }

  function singularize(value) {
    if (value.endsWith('ies')) return `${value.slice(0, -3)}y`
    if (value.endsWith('sses')) return value.slice(0, -2)
    if (value.endsWith('s') && !value.endsWith('ss')) return value.slice(0, -1)
    return value
  }

  function pascalCase(value) {
    return value
      .replace(/\[\]/g, '')
      .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
      .split(/[^A-Za-z0-9]+/)
      .filter(Boolean)
      .map(part => `${part.charAt(0).toUpperCase()}${part.slice(1)}`)
      .join('')
  }

  function typeName(path, rawType, hasChildren) {
    const normalized = rawType.replace(/`/g, '').trim()
    const lower = normalized.toLowerCase()
    const property = localName(path).replace(/\[\]$/, '')

    if (lower.includes('menu action')) return lower.includes('array') ? 'MenuAction[]' : 'MenuAction'
    if (lower.includes('action object')) return 'Action'
    if (lower.includes('result object')) return 'Result'
    if (lower === 'object' && hasChildren) return pascalCase(property)
    if (lower === 'array' && hasChildren) return `${pascalCase(singularize(property))}[]`
    if (lower === 'object') return 'JSON object'
    if (lower === 'array') return `${pascalCase(singularize(property))}[]`
    if (/^array of .*objects?$/.test(lower)) return `${pascalCase(singularize(property))}[]`
    return normalized
  }

  function shapeId(path) {
    return `config-shape-${path
      .replace(/\[\]/g, '-items')
      .replace(/[^A-Za-z0-9]+/g, '-')
      .replace(/^-|-$/g, '')
      .toLowerCase()}`
  }

  function breadcrumb(path) {
    return ['data', ...fieldSegments(path)].join('  →  ')
  }

  function typeHint(path, rawType, hasChildren, values = '') {
    const resolved = typeName(path, rawType, hasChildren)
    if (resolved !== 'JSON object') return resolved
    const objectLiteral = values.match(/\{[^{}]+\}/)?.[0]
    return objectLiteral ? objectLiteral.replace(/"/g, '').replace(/,\s*/g, '; ') : resolved
  }

  function requirementState(required) {
    if (/^no(?:\b|$)/i.test(required.trim())) return { label: 'Optional', modifier: 'optional' }
    if (/^yes(?:\b|$)/i.test(required.trim()) && !/\bwhen\b|\bfor\b/i.test(required)) {
      return { label: 'Required', modifier: 'required' }
    }
    return { label: 'Conditional', modifier: 'conditional' }
  }

  function createGridCell(className, label) {
    const cell = document.createElement('div')
    cell.className = className
    cell.dataset.label = label
    return cell
  }

  function buildPropertyEntry(entry, entriesByPath, depth, localProperty) {
    const record = entriesByPath.get(entry.path)
    const hasChildren = record?.children.length > 0
    const item = hasChildren ? document.createElement('details') : document.createElement('div')
    item.className = hasChildren ? 'neops-config-group' : 'neops-config-item'
    item.style.setProperty('--neops-config-depth', depth)
    if (entry.id || hasChildren) item.id = entry.id || shapeId(entry.path)

    const row = hasChildren ? document.createElement('summary') : document.createElement('div')
    row.className = 'neops-config-row'

    const nameCell = createGridCell('neops-config-name-cell', 'Configuration')
    const disclosure = document.createElement('span')
    disclosure.className = hasChildren ? 'neops-config-disclosure' : 'neops-config-disclosure-placeholder'
    disclosure.setAttribute('aria-hidden', 'true')
    const property = document.createElement('code')
    property.className = 'neops-config-property-name'
    property.textContent = localProperty || depth > 0 ? localName(entry.path).replace(/\[\]$/, '') : entry.path
    property.title = entry.path
    nameCell.append(disclosure, property)

    const typeCell = createGridCell('neops-config-type-cell', 'Type')
    const type = document.createElement('code')
    type.className = 'neops-config-type'
    type.textContent = typeHint(entry.path, entry.type, hasChildren, entry.values)
    typeCell.append(type)

    const state = requirementState(entry.required)
    const requirementCell = createGridCell('neops-config-required-cell', 'Required')
    const requirement = document.createElement('span')
    requirement.className = `neops-config-requirement neops-config-requirement--${state.modifier}`
    requirement.textContent = entry.required
    requirementCell.append(requirement)

    const description = createGridCell('neops-config-property-description', 'Default and effect')
    if (entry.descriptionNodes) {
      description.append(...entry.descriptionNodes.map(node => node.cloneNode(true)))
    } else {
      const descriptionCell = entry.row.cells[entry.row.cells.length - 1]
      description.append(...Array.from(descriptionCell.childNodes).map(node => node.cloneNode(true)))
    }

    row.append(nameCell, typeCell, requirementCell, description)
    item.append(row)

    if (hasChildren) {
      const children = document.createElement('div')
      children.className = 'neops-config-children'
      record.children.forEach(child => {
        children.append(buildPropertyEntry(child, entriesByPath, depth + 1, true))
      })
      item.append(children)
    }

    return item
  }

  function buildPropertyList(entries, entriesByPath, localProperty) {
    const list = document.createElement('div')
    list.className = 'neops-config-property-list'

    const header = document.createElement('div')
    header.className = 'neops-config-list-header'
    ;['Configuration', 'Type', 'Required', 'Default and effect'].forEach(label => {
      const cell = document.createElement('div')
      cell.textContent = label
      header.append(cell)
    })
    list.append(header)

    entries.forEach(entry => {
      list.append(buildPropertyEntry(entry, entriesByPath, 0, localProperty))
    })

    return list
  }

  function parseReferenceTable(table) {
    const headings = Array.from(table.querySelectorAll('thead th')).map(cell => cell.textContent.trim())
    const pathIndex = headings.findIndex(heading => heading === 'Path' || heading === 'Property')
    const typeIndex = headings.indexOf('Type')
    const requiredIndex = headings.indexOf('Required')
    if (pathIndex === -1 || typeIndex === -1 || requiredIndex === -1) return null

    const entries = Array.from(table.querySelectorAll('tbody tr'))
      .map(row => {
        const cells = Array.from(row.cells)
        const path = cells[pathIndex]?.querySelector('code')?.textContent.trim()
        if (!path) return null
        return {
          path,
          type: cells[typeIndex]?.textContent.trim() || 'unknown',
          required: cells[requiredIndex]?.textContent.trim() || 'No',
          row,
        }
      })
      .filter(Boolean)

    if (!entries.length) return null
    return { entries, headings, pathHeading: headings[pathIndex] }
  }

  function enhanceReferenceTable(table) {
    if (table.hasAttribute(enhancedAttribute)) return
    const parsed = parseReferenceTable(table)
    if (!parsed) return

    const entriesByPath = new Map(parsed.entries.map(entry => [entry.path, { ...entry, children: [] }]))
    for (const entry of entriesByPath.values()) {
      const parent = findParentEntry(entriesByPath, entry.path)
      if (parent) parent.children.push(entry)
    }

    const minimumDepth = Math.min(...parsed.entries.map(entry => fieldDepth(entry.path)))
    const roots = parsed.entries.filter(entry => fieldDepth(entry.path) === minimumDepth)
    const rootContext = commonPath(roots.map(entry => parentPath(entry.path)))

    const reference = document.createElement('section')
    reference.className = 'neops-config-reference'
    reference.setAttribute(enhancedAttribute, 'true')

    if (parsed.pathHeading === 'Path') {
      const pathGuide = document.createElement('div')
      pathGuide.className = 'neops-config-path-guide'
      const pathLabel = document.createElement('span')
      pathLabel.textContent = 'Paths start at'
      const path = document.createElement('code')
      path.className = 'neops-config-context'
      path.textContent = breadcrumb(rootContext)
      const pathHelp = document.createElement('span')
      pathHelp.innerHTML = '<code>[]</code> means one item in an array.'
      pathGuide.append(pathLabel, path, pathHelp)
      reference.append(pathGuide)
    }

    reference.append(buildPropertyList(roots, entriesByPath, Boolean(rootContext)))

    const tableWrapper = table.closest('.md-typeset__scrollwrap')
    if (tableWrapper && tableWrapper.querySelectorAll('table').length === 1) {
      tableWrapper.replaceWith(reference)
    } else {
      table.replaceWith(reference)
    }
  }

  function fieldMetadata(heading) {
    let sibling = heading.nextElementSibling
    while (sibling && !/^H[23]$/.test(sibling.tagName)) {
      const table = sibling.tagName === 'TABLE' ? sibling : sibling.querySelector('table')
      if (table) {
        const metadata = {}
        Array.from(table.querySelectorAll('tbody tr')).forEach(row => {
          const cells = row.cells
          if (cells.length >= 2) metadata[cells[0].textContent.trim()] = cells[1].textContent.trim()
        })
        return { metadata, table, anchor: sibling }
      }
      sibling = sibling.nextElementSibling
    }
    return { metadata: {}, table: null, anchor: null }
  }

  function enhanceFieldSections(article) {
    const configurationHeading = article.querySelector('h2#configuration')
    if (!configurationHeading) return

    const fieldHeadings = []
    let sectionNode = configurationHeading.nextElementSibling
    while (sectionNode && sectionNode.tagName !== 'H2') {
      if (sectionNode.tagName === 'H3' && sectionNode.querySelector('code')) fieldHeadings.push(sectionNode)
      sectionNode = sectionNode.nextElementSibling
    }
    if (!fieldHeadings.length) return

    const entries = fieldHeadings
      .map(heading => {
        const path = heading.querySelector('code')?.textContent.trim()
        const { metadata, table, anchor } = fieldMetadata(heading)
        if (!path || !table || !anchor) return null

        const defaultValue = document.createElement('span')
        defaultValue.className = 'neops-config-default'
        defaultValue.textContent = metadata.Default || 'No default documented'

        const descriptionNodes = [defaultValue]
        let effectNode = anchor.nextElementSibling
        while (effectNode && !/^H[23]$/.test(effectNode.tagName)) {
          descriptionNodes.push(effectNode.cloneNode(true))
          effectNode = effectNode.nextElementSibling
        }

        return {
          id: heading.id,
          path,
          type: metadata.Type || 'unknown',
          required: metadata.Required || 'No',
          values: metadata.Values || '',
          descriptionNodes,
        }
      })
      .filter(Boolean)
    if (!entries.length) return

    const entriesByPath = new Map(entries.map(entry => [entry.path, { ...entry, children: [] }]))
    for (const entry of entriesByPath.values()) {
      const parent = findParentEntry(entriesByPath, entry.path)
      if (parent) parent.children.push(entry)
    }
    const minimumDepth = Math.min(...entries.map(entry => fieldDepth(entry.path)))
    const roots = entries.filter(entry => fieldDepth(entry.path) === minimumDepth)

    const reference = document.createElement('section')
    reference.className = 'neops-config-reference'
    reference.setAttribute(enhancedAttribute, 'true')

    const pathGuide = document.createElement('div')
    pathGuide.className = 'neops-config-path-guide'
    const pathLabel = document.createElement('span')
    pathLabel.textContent = 'Paths start at'
    const path = document.createElement('code')
    path.className = 'neops-config-context'
    path.textContent = 'data'
    const pathHelp = document.createElement('span')
    pathHelp.innerHTML = '<code>[]</code> means one item in an array.'
    pathGuide.append(pathLabel, path, pathHelp)
    reference.append(pathGuide, buildPropertyList(roots, entriesByPath, false))

    const firstHeading = fieldHeadings[0]
    firstHeading.before(reference)
    let node = firstHeading
    while (node && node !== sectionNode) {
      const next = node.nextElementSibling
      node.remove()
      node = next
    }
  }

  function openHashTarget() {
    const target = window.location.hash ? document.querySelector(window.location.hash) : null
    if (!target) return
    let parent = target
    while (parent) {
      if (parent.tagName === 'DETAILS') parent.open = true
      parent = parent.parentElement
    }
  }

  function enhanceConfigurationReference() {
    const article = document.querySelector('article') || document.querySelector('.md-content')
    if (!article) return
    article.querySelectorAll('table').forEach(enhanceReferenceTable)
    enhanceFieldSections(article)
    openHashTarget()
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(enhanceConfigurationReference)
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', enhanceConfigurationReference, { once: true })
  } else {
    enhanceConfigurationReference()
  }

  window.addEventListener('hashchange', openHashTarget)
})()
