#Pybookie

Pybookie is booking client based on multiagent systems that provides analyisis of teams and reccomends betting options.

It consists of one master and N client agents that comunicate with each other.

Master agent analyizes teams based on data from 2014 WC in Brazil:
[https://github.com/openfootball/world-cup](https://github.com/openfootball/world-cup)


##Configuration instructions
Required:

	Python 2.7
	Spade
	Requests


##Installation instructions

    ~ configure.py localhost
    
    ~ runspade.py
    
#### Run these cmds in parallel    
    
    ~ python client.py
    
    ~ python server.py


##Future work
- implementation of last 10 games for specific team
- get goals for currently active players
- add wikipedia support
 
##Credits and acknowledgements

Author: [lovro_p](https://twitter.com/lovro_p)

###Changelog

**v 1.0** - 5.6.2016 - Initial version made for VAS (Višeagentni sustavi - Multiagent systems - faculty of organization and informatics 2016)


###Copyright and licensing information
Apache licence
