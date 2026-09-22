;(function () {
  const minimumHeight = 480
  const maximumHeight = 2400

  window.addEventListener('message', event => {
    if (event.origin !== window.location.origin) return
    if (event.data?.source !== 'neops-card-lab' || event.data?.type !== 'resize') return
    if (!Number.isFinite(event.data.height)) return

    const frame = Array.from(document.querySelectorAll('iframe.neops-card-lab-frame')).find(
      candidate => candidate.contentWindow === event.source
    )
    if (!frame) return

    const contentHeight = Math.min(maximumHeight, Math.max(minimumHeight, Math.ceil(event.data.height)))
    const borderHeight = frame.offsetHeight - frame.clientHeight
    frame.style.height = `${contentHeight + borderHeight}px`
  })
})()
