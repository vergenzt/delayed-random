# delayed-random

At my last internship we played a _remote_ game of [Werewolf][1] (also known as
Mafia). Because it wasn't working out so well (it's hard to play if you can't
see the people you're trying to read), we eventually just resorted to deciding
who to lynch randomly.

However, problems arise with trusting any particular party to generate an honest
random number. Even if they provide a link to a [random.org][2]-generated
number, there's still a question of whether they kept generating them until they
got the desired result.

So, this app aimed to solve this problem, by allowing one to create a permalink
with a specific pre-determined time when it will provide the random number. This
allows parties to agree that it will be the authoritative source _before_ it has
provided the number, and avoid issues of trust (assuming that the host of the
app is trustworthy).

However, it's nowhere near done.

[1]: http://en.wikipedia.org/wiki/Mafia_(party_game)
[2]: http://www.random.org/

