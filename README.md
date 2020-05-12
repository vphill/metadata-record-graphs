# metadata-record-graphs
Code to support a dissertation on metadata analysis.

# Running the code

This code is designed to run on data that is formatted in a specific way. 

First off you will need a list of all of the identifiers in your dataset. I suggest calling this file `nodes.txt`

For example, this is the `nodes.txt` file from the test directory.

```
A
B
C
D
E
F
```

Second, you will need your data as two columns separated by a tab character.  The first column is the identifier and the second column is the data value you will use to connect identifiers with.  Here is an example of `subject_ark_value.txt` from the test directory.

```
A	Dog
B	Dog
D	Dog
B	Cat
D	Cat
C	Cat
E	Shark
```

# Test

You can run the tests 
