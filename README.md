# PRIMRE-A

This work aims to help users access the already-public Portal and Repository for Information on Marine Renewable Energy ([PRIMRE](https://openei.org/wiki/PRIMRE/)) APIs. It is therefore called PRIMRE-Access (PRIMRE-A). The main functionality of the package is to compose the data accessible from the [Tethys](https://tethys.pnnl.gov/), [Tethys Engineering](https://tethys-engineering.pnnl.gov/), Marine Hydrokinetic Data Repository ([MHKDR](https://mhkdr.openei.org/)) and [Marine Energy Projects Database](https://openei.org/wiki/PRIMRE/Databases/Projects_Database) APIs into a relational database structure to facilitate data usage across knowledge hubs.

The completed feature set includes a partial implementation of the database schema on the Tethys and Tethys Engineering knowledge hubs, and data documentation/exploration in preparation for the implementation on MHKDR.

## Contents

- development_notebooks : Contains python notebooks for the purposes of feature development for the package, and are retained here to aid future development
- primrea : Package code
- PRIMRE KHs tabular structure : Database diagrams

## Installation

PRIMRE-A can be installed from PyPi using pip:

```bash
pip install primrea
```

## Usage

To access the database created by PRIMRE-A, one must first import the package core:

```bash
from primrea import core
```

and then initialize the database using:

```bash
primre_data = core.primrea_data
```

It is normal for this second line of code to take some time to execute, as the package is retrieving all content associated with the implemented PRIMRE knowledge hubs and transforming it into the cleaned tables.

## Database Schema

Below is the ER diagram corresponding to the full PRIMRE-A database schema. 

![](full_ER.svg)