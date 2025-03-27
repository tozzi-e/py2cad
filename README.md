Example of using the build123d python library to create a STEP file of a sensor part.
Uses the OCP CAD viewer extension (ocp_vscode) to see the part in a window of VS code as it is built.
I used the "algebra mode" of build123d.
The part is built in stages, first a rounded rectangle is extruded.
Then various  cylindrical volumes are subtracted from this part.
A fillet operation is included. The fillet requires selecting an edge which involves getting the edge
from a list of all edges which are then filtered by by size, or other characteristics, this may involve trial and error. 
The filtering needed may need to be re-done if the code before the fillet has changes big enough that they modify the list of edges. 
To avoid issues a potential strategy could be to create the fillets reasonably early in the code 
such that: 
1-the edge is easier to find
2-Further downstream operations can be tweaked and they will not affect the edges from the fillets.
