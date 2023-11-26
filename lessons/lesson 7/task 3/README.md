# Task 3

Planets revolve around stars in elliptical orbits. Let's call the farthest planet
the one whose orbit has the largest area. Write a function `find_farthest_orbit(list_of_orbits)`,
which among the list of orbits of planets will find the one on which the most distant
planet rotates. Do not take into account circular orbits: you know that your star
does not have such planets, but artificial satellites have been launched into circular
orbits. The result of the function should be a tuple containing the lengths of the
semi-axes of the ellipse of the orbit of the farthest planet. Each orbit is a tuple
of a pair of numbers - the semi-axes of its ellipse. The area of the ellipse is calculated
by the formula `S = piab`, where `a` and `b` are the lengths of the semi-axes of
the ellipse. When solving a problem, use list expressions. Hint: the easiest way
is to find an ellipse in two steps: first calculate the largest area of the ellipse,
and then find the ellipse itself having such an area. It is guaranteed that the farthest
planet is exactly one.

## Example

- `[(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]` -> `(2.5, 10)`
