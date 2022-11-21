def linearBezier(p1:tuple[float, float], p2:tuple[float, float], t:float, rounded=True)->tuple[float, float]:
    """
    Gives the cordinates of a line between 2 points in a plane at the time frame 't'
    Source: https://en.wikipedia.org/wiki/B%C3%A9zier_curve

    Attributes
    ----------
    p1 : tuple[float, float]
        Cordinates of the first point of the line
    p2 : tuple[float, float]
        Cordinates of the last point of the line
    t : float
        The Time Frame
    rounded : bool
        If the result returned should be rounded or not (default True)
    """
    x = ((1-t)*p1[0]) + (t*p2[0])
    y = ((1-t)*p1[1]) + (t*p2[1])
    if rounded:
        x = round(x)
        y = round(y)
    return (x,y)

def quadraticBezier(p1:tuple[float, float], p2:tuple[float, float], c:tuple[float, float], t:float, rounded=True)->tuple[float, float]:
    """
    Gives the cordinates of a line between 2 points in a plane at the time frame 't'
    Source: https://en.wikipedia.org/wiki/B%C3%A9zier_curve

    Attributes
    ----------
    p1 : tuple[float, float]
        Cordinates of the first point of the line
    p2 : tuple[float, float]
        Cordinates of the last point of the line
    c : tuple[float, float]
        Cordinates of the control point of the line
    t : float
        The Time Frame
    rounded : bool
        If the result returned should be rounded or not (default True)
    """
    x = ( (1-t) * ( ( (1-t)  *p1[0] ) + ( t * (c[0]) ) ) ) + ( t*( ((1-t) * c[0] ) + (t*p2[0])) )
    y = ( (1-t) * ( ( (1-t)  *p1[1] ) + ( t * (c[1]) ) ) ) + ( t*( ((1-t) * c[1] ) + (t*p2[1])) )

    if rounded:
        x = round(x)
        y = round(y)
    return (x,y)

def cubicBezier(p1:tuple[float, float], p2:tuple[float, float], c1:tuple[float, float], c2:tuple[float, float], t:float, rounded=True)->tuple[float, float]:
    """
    Gives the cordinates of a line between 2 points in a plane at the time frame 't'
    Source: https://en.wikipedia.org/wiki/B%C3%A9zier_curve

    Attributes
    ----------
    p1 : tuple[float, float]
        Cordinates of the first point of the line
    p2 : tuple[float, float]
        Cordinates of the last point of the line
    c1 : tuple[float, float]
        Cordinates of the first control point of the line
    c 1: tuple[float, float]
        Cordinates of the second control point of the line
    t : float
        The Time Frame
    rounded : bool
        If the result returned should be rounded or not (default True)
    """
    x = ( ( ((1-t)**3) * p1[0]) + ( (3 * ( (1-t)**2 ) ) * t * c1[0] ) + ( 3 * (1-t) * t * t * c2[0] ) + ( (t**3) * p2[0] ) )
    y = ( ( ((1-t)**3) * p1[1]) + ( (3 * ( (1-t)**2 ) ) * t * c1[1] ) + ( 3 * (1-t) * t * t * c2[1] ) + ( (t**3) * p2[1] ) )

    if rounded:
        x = round(x)
        y = round(y)
    return (x,y)

