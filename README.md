# Screenshots organizer
- Simple script to take screenshots (of the active window) and save them in folders determined by the time of the shot. 
- At the moment it works for Ubuntu only (and other gnome-based distributions maybe), but the concept is easy to adapt to ther systems. It doesn't need any libraries, and
uses `genome-screenshot` to take the pictures.

## Usage
- To set it up, you have to edit the `config.json` file. There, you can add a default folder, where the screenshots will be saved if the time does not match any of the other folders. Then follow the example of `config.example.json` to add your custom times and folders.
- To use it, I added a keyboard shortcut in Ubuntu, so that it's executed whenever I like, just as a normal screenshot.
