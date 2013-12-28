#rdfcli

rdfcli is a command-line Linked Data browser. It allows to visit RDF resources, see their links and follow them across different datasets. The user interface is based on a stateful command line, much like a shell to browse a file system.

It is similar in functionality to other RDF browsers like [Disco](http://wifo5-03.informatik.uni-mannheim.de/bizer/ng4j/disco/) or [Tabulator](http://www.w3.org/2005/ajar/tab), but limited to the basic features. When a resource is visited, the URI is dereferenced and the returned triples are loaded to the local graph. The user can then explore the outoing and incoming predicates of the current resource, and navigate to their objects or subjects.

rdfcli uses the Python [rdflib](https://github.com/RDFLib/rdflib) library to handle RDF data.

##Installation

```
# clone repo
$ git clone git@github.com:rrasmo/rdfcli.git
$ cd rdfcli
# (optional) make a virtualenv
$ virtualenv venv
$ . venv/bin/activate
# install dependencies
$ pip install -r requirements
```

##Usage

```
$ rdfcli
> help

Commands:

  load URI    # Load triples from URI or file.
  go URI      # Go to a resource and load related triples.
  size        # Print the number of triples in the graph.
  types       # List all types, i.e. objects of rdf:type.
  this        # Print the current resource.
  pred        # List all predicates of the current resource.
  ls [PRED]   # List outgoing predicates and objects. If a predicate is given, print the objects.
  fw PRED     # Follow outgoing predicate, go to the object.
  is [PRED]   # List incoming subjects and predicates. If a predicate is given, print the subjects.
  bw PRED     # Follow backwards incoming predicate, go to the subject.
  f           # Go forward in history
  b           # Go back in history
  hist        # Print history stack.
  help        # Print this help.
  exit        # Exit.

> go http://dbpedia.org/resource/Metallica
http://dbpedia.org/resource/Metallica> size
812
http://dbpedia.org/resource/Metallica> ls
    rdf:type
        dbpedia-owl:Band
    rdfs:label
        <Metallica>
    dbpedia-owl:bandMember
        <http://dbpedia.org/resource/James_Hetfield>
    ...
http://dbpedia.org/resource/Metallica> ls dbpedia-owl:bandMember
    <http://dbpedia.org/resource/Kirk_Hammett>
    <http://dbpedia.org/resource/James_Hetfield>
    <http://dbpedia.org/resource/Lars_Ulrich>
    <http://dbpedia.org/resource/Robert_Trujillo>
http://dbpedia.org/resource/Metallica> fw dbpedia-owl:bandMember
    0) http://dbpedia.org/resource/Kirk_Hammett
    1) http://dbpedia.org/resource/James_Hetfield
    2) http://dbpedia.org/resource/Lars_Ulrich
    3) http://dbpedia.org/resource/Robert_Trujillo
Select one resource: 0
http://dbpedia.org/resource/Kirk_Hammett> is
    <http://dbpedia.org/resource/Master_of_Puppets>
        dbpprop:artist
    <http://dbpedia.org/resource/Metallica>
        dbpedia-owl:bandMember
    ...
http://dbpedia.org/resource/Kirk_Hammett> is dbpedia-owl:bandMember
    <http://dbpedia.org/resource/Metallica>
http://dbpedia.org/resource/Kirk_Hammett> bw dbpedia-owl:bandMember
http://dbpedia.org/resource/Metallica> f
http://dbpedia.org/resource/Kirk_Hammett> b
http://dbpedia.org/resource/Metallica>
```
