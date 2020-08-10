import math

NotImplementedErrorComparisonMessage = 'Comparison must be done between polygon objects'

class Polygon():
    def __init__(self, edge_count, circumradius):
        if edge_count < 3:
            raise ValueError('Polygons must have at least 3 sides')
        self._edges = tuple(f'e{n}' for n in range(edge_count))
        self._vertices = tuple(f'v{n}' for n in range(edge_count))
        self._circumradius = circumradius


    @property
    def edges(self):
        return self._edges


    @property
    def edge_count(self):
        return len(self._edges)
    

    @property
    def vertices(self):
        return self._vertices


    @property
    def vertex_count(self):
        return len(self._vertices)


    @property
    def circumradius(self):
        return self._circumradius


    @property
    def interior_angle(self):
        return ( self.edge_count - 2 ) * ( 180 / self.edge_count )


    @property
    def edge_length(self):
        return ( 2 * self.circumradius ) * math.sin(math.pi / self.edge_count) 


    @property
    def apothem(self):
        return ( self.circumradius * math.cos((math.pi / self.edge_count)) )


    @property
    def area(self):
        return ( .5 * self.edge_count * self.edge_length * self.apothem )


    @property
    def perimeter(self):
        return ( self.edge_count * self.edge_length )


    def __repr__(self):
        return f'Polygon ({self.edge_count} edges of length {round(self.edge_length, 2)})'


    def __eq__(self, polygon2):
        if not isinstance(polygon2, Polygon):
            raise NotImplementedError(NotImplementedErrorComparisonMessage)
        
        if (
            self.vertex_count == polygon2.vertex_count
            and self.circumradius == polygon2.circumradius
        ):
            return True
        else:
            return False
    

    def __gt__(self, polygon2):
        if not isinstance(polygon2, Polygon):
            raise NotImplementedError(NotImplementedErrorComparisonMessage)


        if ( self.vertex_count > polygon2.vertex_count ):
            return True
        else:
            return False

