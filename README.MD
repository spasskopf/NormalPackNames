# Features
 - Cleans resource pack names by removing "!" and " " from the beginning of the name
 - Scans packs for invalid pack.mcmeta files and invalid structure

# Cleaning Resource Pack Names
## Example

Some pack makers like to add characters to the pack name in order for it to appear first:  
Just a few examples

```text
!          §bShant§3V4 §6REVAMP §3[32x].zip
!                   §bThe§6Legend§327 [16x] §6REVAMP.zip
!                     §6ST Patrick §0[64x] §0.zip
!                    §8-§bA§3o §fShikuro§8 [§f32x§8].zip
!                    §91.14 default edit Dark Blue.zip
!                    §bAvail §6[32x].zip
!                  §bDefault §3[32x] Thick Sword.zip
```

This tool removes leading symbols ("!" and " ") which turns these names into the following:

```text
§6ST Patrick §0[64x] §0.zip
§8-§bA§3o §fShikuro§8 [§f32x§8].zip
§91.14 default edit Dark Blue.zip
§bAvail §6[32x].zip
§bDefault §3[32x] Thick Sword.zip
§bShant§3V4 §6REVAMP §3[32x].zip
§bThe§6Legend§327 [16x] §6REVAMP.zip
```

# Scanning Resource Packs
Sometimes there are invalid pack.mcmeta files in a resource pack preventing it from showing in the pack menu.
If you are using [aycy's resource pack manager mod v1.2](https://www.youtube.com/watch?v=OQZFWrrEcYM) this can go as far as not loading any subdirectories because of one invalid file.

This tool scans your resource pack directory and reports any broken files.
More information about this can be found [here](https://github.com/spasskopf/Pack-Tools/wiki/Checking-Resource-Packs-for-invalid-pack.mcmeta-files)

# Usage

1. Download the python file (`main.py`)
2. Copy the path to the pack-directory   
    Default resourcepack directory on Windows:
   ```
   C:\Users\USERNAME\AppData\Roaming\.minecraft\resourcepacks
    ```
3. Open a command prompt / terminal (`cmd` on windows)
4. Run the python file (examples below)
   
The program processes every directory provided recursively  

## Options
* --verbose / -v
  * Outputs more information about the programs current status. _Might_ spam your console
* --search / -s
  * Searches for invalid resource packs
* --clean / -c
  * Cleans resource packs names
* --help / -h
  * Prints help
```shell
#Cleans the User's resourcepack directory and sets the output mode to verbose
python main.py -cv C:\Users\USERNAME\AppData\Roaming\.minecraft\resourcepacks
#Scans a relative directory for invalid resource packs
python main.py --search relative/directory
#Should also work on linux :)
python main.py -csv /gnu/linux/minecraft/resourcepacks
#Cleans and scans 3 directories
python main.py -cs directory1 directory2 directory3
```

