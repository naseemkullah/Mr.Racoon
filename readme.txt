Welcome to gift_exchange!

For family members who would like to register for the gift exchange, 
please type the following command:

$ ./gift_exchange --register

You will need to provide your name, followed by the name of your partner if you have one.
If you are single, just leave the answer blank.

The registration information is kept in a local file called family.json.
In case of file corruption or for any other reason where you would like to restart the registration process, simply delete family.json.

To successfully run the gift exchange, there should be at least 2 registered members who are not a couple
or at least 4 members if there is at least one couple.

Once everyone has registered, the gift exchange process can start by running:

$ ./gift_echange --run

If you would like to run some tests on the code please ensure that pytest is installed and run pytest from within the directory.
This will run tests on both gift_exchange.py and it's state of the art algorithm randraw.py

Enjoy!

