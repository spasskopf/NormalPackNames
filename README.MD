Cleans resource pack names by removing "!" and " " from the beginning of the name

# Example

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

# Usage

1. Download the python file (`main.py`)
2. Copy the path to the pack-directory   
    Default resourcepack directory on Windows:
   ```
   C:\Users\USERNAME\AppData\Roaming\.minecraft\resourcepacks
    ```
3. Open a command prompt / terminal (`cmd` on windows)
4. Run the python file (examples below)
   
The program processes every provided directory  
There are currently no other options
```commandline
python main.py C:\Users\USERNAME\AppData\Roaming\.minecraft\resourcepacks
python main.py relative/directory
python main.py /gnu/linux/minecraft/resourcepacks
python main.py directory1 directory2 directory3
```

