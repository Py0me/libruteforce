# LibruteForce <br/><sub>(Totally not a super powerful Bruteforcing library written in the very popular Python programming language by super professional hackers.)</sub> #
- - - -
## Capabilities ##

  - ### Version 1.0: ###
    - [x] Random User Agent string selector
      - [x] RandomArray data type
      - [x] Default User Agent list
    - [ ] Full HTTP protocol library implementation
    - [ ] Full HTTPS protocol library implementation
    - [ ] Full Zombie protocol library implementation
    - [ ] Full `ReFresh` attack implementation
    - [ ] Full `DoS` attack implementation
    - [ ] Basic `DDoS` attack implementation
      - [ ] Full Zombie protocol support
      - [ ] Basic HTTP &amp; HTTPS protocol support
      - [ ] Master authentication support
      - [ ] Full Master class implementation
      - [ ] Full Router class implementation
      - [ ] Full Zombie class implementation
    - [ ] Full `URL` attack implementation
      - [ ] Full HTTP &amp; HTTPS protocol support
    - [ ] Full `LogIn` attack implementation
    - [ ] Basic `Passwrd` attack implementation
    - [ ] Basic `SearchHTML`  attack implementation
    
- - - -
## BruteForce class ##
*From module `/libruteforce/__init__.py`:*

From the internal Python `help()` documentation:

```
Attack Types (case insensitive):
        ReFresh -
                Performs as many requests on the target as possible. Response
                data will not be saved and only stored temporarily to allow
                accurate updating of counters, following redirects, etc.
                If redirects are enabled, the redirected resources are saved
                in folders corresponding to their returned status code and
                prefixed (abcd.) with their hash representation as to prevent
                files from being overriden or duplicated.

        DoS -
                Simmilar to the ReFresh attack, but tries to direct as much traffic
                to the target as possible. Everything in this method is optimized
                for speed and quantity of the request. No response data will be
                received, and, if supported, UDP mode will be enabled. DoS is
                the shorter term for Denial of Service, a type of attack which
                has been around for a long time and has been well documented by
                other sources, so there is not as much detail provided here.

        DDoS -
                A modified variant of the DoS attack. Uses a decentralized network
                of zombie computers, which may be created using the methods of the
                ZombieDDoS class in the ddos module. All zombies are controlled
                by the 'master', a server which functions like a router for all
                the instructions that are comming from the master computer. The
                master computer may also be the router, though this is not recommended
                due to potential identity leaks or security concerns. Having the
                master computer seperated from the router also has the benefit of
                being able to query multiple servers at the same time which may
                be used to activate the zombie network.

        URL -
                Runs through a word list or randomly generated text strings.
                All responses other than 404 errors will be saved in folders
                corresponding to the returned status code. Headers may be saved
                as well if so requested by the user.

        LogIn -
                Sends continuous requests to a login page until a non-error status
                is returned. Supports word lists and randomly generated text strings.

        Passwrd -
                Runs through a list of password hashes and tries to crack them one by
                one using either word lists or randomly generated text strings.

        SearchHTML -
                Runs through a list of HTML resources and saves all pages containing the
                specified search string to disk. Two types of mode are available for this
                attack, the first one being the scanning of multiple targets and the second
                one parsing all encountered documents and subsequently following all links
                found on the page ('scraping' and 'indexing' the website). The latter may
                take very long depending on the size of the website, which is why this
                specific mode has a variety of flags available to operate more efficiently.
                Those flags include, but are not limited to: maximum nesting depth, follow
                external hosts, exclude URLs, ignore status XXX, etc.
```

- - - -
## RandomArray class ##
*From module `/libruteforce/__init__.py`:*

No documentation available for now. We're sorry for that :cry:

- - - -
## MasterDDoS class ##
*From module `/libruteforce/ddos.py`:*


No documentation available for now. We're sorry for that :cry:

- - - -
## RouterDDoS class ##
*From module `/libruteforce/ddos.py`:*


No documentation available for now. We're sorry for that :cry:

- - - -
## ZombieDDoS class ##
*From module `/libruteforce/ddos.py`:*


No documentation available for now. We're sorry for that :cry:
