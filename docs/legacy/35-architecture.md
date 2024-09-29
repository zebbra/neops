# Architecture

## Principles

neops.io as a network automation software was built with the following principles in mind

- network engineers know their network best, so network design and logic of tasks/todo’s are in their responsibility
- neops.io itself has no, or as minimalistic as possible, knowledge of the network and the functionality of its devices. Information and logic about the network is brought to neops.io by tasks that are collecting information from the network or external systems.
- Facts are a central element in neops.io. They are the base upon to build the logic of tasks to deploy changes in the network
- neops.io should bring flexibility to implement functionality at different levels
  - device level: change the methods of how to read and write from network devices to fit your vendors and your needs
  - provider level: bring your own task providers to implement APIs of your peripheral systems or bring new features (like AI ;)) to neops.io
  - task level: define the todo in your network within your tasks, so they will represent the prerequisites of your network
  - permission, workflow level (planned) and triggers (planned): easy automate or delegate tasks

## Services

### Logical application overview

```mermaid
graph TD
    f1([Frontend])
    b1([Backend])
    w1([Worker])
    w2([Worker])
    db1[(Postgres)]
    db2[(Elastic)]
    n1[Network Devices]
    n2[Network Devices]
    f1 --> | GraphQL | b1
    b1 --> db1
    b1 --> db2
    b1 --- | Redis | w1
    b1 --- | Redis | w2
    w1 --> db1
    w1 --> db2
    w2 --> db1
    w2 --> db2
    w1 --> n1
    w2 --> n1
    w1 --> n2
    w2 --> n2
```

### Containers

We ship one container with different functionality. Frontend (VueJS) and Backend (python) are packed in one container.

Depending on its start parameters the neops.io container runs as:

- Frontend/Backend
- Worker
- Scheduler

neops.io depends on external ressources/services/containers:

- [Redis](https://redis.io/) - _message brocker between backend/worker/scheduler_
- [Postgres](https://www.postgresql.org/) - _relational database_
- [Elastic Search](https://www.elastic.co/elasticsearch/) - _search database_
- [Keycloak](https://www.keycloak.org/) - _authentication service_

```mermaid
graph TD
    rp([Traefik Reverse Proxy])
    bf1([neops.io Backend/Frontend])
    bf2([neops.io Backend/Frontend])
    w1([neops.io Worker])
    w2([neops.io Worker])
    s1([neops.io Scheduler])
    db1[(Postgres)]
    db2[(Elastic)]
    r1[(Redis)]
    a1([Authentication/Keycloak])
    rp --> bf1
    rp --> bf2
    bf1 & bf2 --> r1
    r1 --> w1 & w2
    bf1 & bf2 --- db1
    bf1 & bf2 --- db2
    w1 & w2 --- db1
    w1 & w2 --- db2
    s1 --- db1
    s1 --> r1
    bf1 & bf2 --> a1

    style bf1 stroke,stroke-dasharray: 5, 5
    style w1 stroke,stroke-dasharray: 5, 5
```

### Scaling/Redundancy

neops.io has all its persistent data in the database, so neops.io containers can be easily run in parallel for scaling reasons.

For scaling and/or redundancy setup of 3rd party applications (Postgres, Elastic Search, Redis and Keycloak) please refer to their documentation.

## Entities

In reference to network components neops.io is currently working with the following entities:

- Device Groups - _Entity to group devices_
- Devices - _Main entity to access network components_
- Interfaces - _Entity for interconnecting Devices_
- Clients - _Entity connected to the network_

Locations are Device Groups with additional properties like address and coordinates.

## Frontend

The frontend is build with [Vue.js](https://vuejs.org) and accesses the backend over a GraphQL API.

## Backend

Backend is based on Python and realized with [Django](https://www.djangoproject.com/), [Celery](http://www.celeryproject.org/) and [nornir](https://nornir.readthedocs.io/) as its main components.

### Models

most relevant database models:

```mermaid
classDiagram
    Interface "1" -- "1" Interface
    Device "1" -- "n" Interface
    Device "n" -- "1" Platform
    Platform "n" -- "n" Library
    DeviceGroup "n" -- "n" Device
    DeviceGroup -- Location
    ProcessExecution "1" -- "n" Execution
    Execution "1" -- "n" DeviceExecution
    Execution "n" -- "1" Task
    DeviceExecution "n" -- "1" Device
    Execution "1" -- "n" DeviceExecutionResult
    Device "1" -- "n" DeviceExecutionResult
    Execution "1" -- "n" DeviceGroupExecutionResult
    DeviceGroup "1" -- "n" DeviceGroupExecutionResult
    Execution "1" -- "n" InterfaceExecutionResult
    Interface "1" -- "n" InterfaceExecutionResult
    Execution "1" -- "n" ClientExecutionResult
    Client "1" -- "n" ClientExecutionResult
    Device "1" -- "n" DeviceConfiguration
    Interface "1" -- "n" InterfaceConfiguration
    Client "1" -- "n" Interface
    Client "n" -- "1" Location

    class ProcessExecution{
        name
    }
    class Execution{
        state
    }
    class DeviceExecution{
        state
        log
    }
    class DeviceExecutionResult{
        state
        message
    }
    class DeviceGroupExecutionResult{
        state
        message
    }
    class InterfaceExecutionResult{
        state
        message
    }
    class ClientExecutionResult{
        state
        message
    }
    class Device{
        hostname
        ip
        facts
    }
    class Platform{
        name
    }
    class Library{
        name
    }
    class Interface{
        name
        neighbor
        facts
    }
    class Client{
        mac
        facts
    }
    class DeviceGroup{
        name
        facts
    }
    class Task{
        name
        provider
        task arguments
    }
    class DeviceConfiguration{
        date
        configuration
    }
    class InterfaceConfiguration{
        date
        configuration
    }
    class Location {
        address
        lon/lat
    }

```

#### Documents

DeviceGroup, Device, Interface and Clients including their facts are stored as separated Indexes in Elastic Search

### Workers/Celery

Celery is used for the Workers they are executing the neops.io [Tasks/Providers](/25-provider).
The workers have direct access to the databases. Scheduled tasks are distributed with a redis queue. To inform the Frontend about updated information GraphQL subscription updates are triggered over different redis queues.

### GraphQL API

All backend Operations are available over the GraphQL API. Testing and Documentation of the API is provided by [GraphiQL](https://github.com/graphql/graphiql) on your installation under `http(s)://NEOPS_URL/graphiql/`

### nornir/Tasks/Providers

see [provider](/25-provider)

## Style Guide

We use flake8 linting and black formatting in the backend and eslint in the frontend to style our code.
