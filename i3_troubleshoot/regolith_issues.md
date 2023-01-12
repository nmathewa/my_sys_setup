# Uninstalling regolith completely

1. Log out of the Regolith session and into the default Ubuntu session.
    ```BASH
    $ sudo apt purge regolith-desktop && sudo apt autoremov
    ```

2. get all regolith related packages 

    ```BASH
    apt list --installed | grep regolith
    ```

3. Remove those packages manually using **apt remove**

4. Remove installed i3 package

    ```BASH
    apt list --installed | grep i3
    ```
> make sure that you are removing the packages related to regolith and i3 

5. log out and log in you are good to go

