from collections import namedtuple

person = namedtuple("Person", ["email", "first_name", "last_name", "age"])

data = {
    1: person("johndoes@gmail.com", "John", "Doe", 23),
    2: person("jerryblue@gmail.com", "Jerry", "Blue", 24),
    3: person("jasonross@gmail.com", "Jason", "Ross", 25),
    4: person("brucewayne@gmail.com", "Bruce", "Wayne", 28),
}
