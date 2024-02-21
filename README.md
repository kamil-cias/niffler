# Niffler is an application for searching public SSH keys in the system.
*Author: Kamil Ciaś, <kamil.cias@goto.systems>*

*GPL-3.0 license*
*This script is distributed under the terms of the GNU General Public License, version 3.0 or later.
Details of the license can be found at: [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)*

## Description
Niffler - a black, fluffy creature with a long muzzle known from the Harry Potter novels.
Nifflers were looking for hidden treasures. The niffler application searches for public SSH keys in both standard locations and the custom locations option using the --anywhere parameter. The purpose of creating the application was to obtain information, especially about hidden public SSH keys.

> The niffler application is invoked from the root user because it requires access to user directories, and when invoked with the --anywhere parameter, to all system files.

## Installation

To install and run the project, you need to change the file permissions with `chmod +x niffler` and move it to the `/usr/bin/` directory. Here are the commands you need to run:

```bash
git clone https://github.com/kamil-cias/niffler
cd niffler
chmod +x niffler
sudo mv niffler /usr/bin/
```

### Using from the root user

```bash
niffler
```
or
> Future functionality

```bash
niffler --anywhere
```

## Call example

```bash
Public SSH key availability report for the host: asgard.home
Report data: Wed Feb 21 01:45:00 PM CET 2024
Call the [--anywhere] parameter to search in non-standard locations.

Users           | Home directory       | Shell           | Keys | Key algorithm        | Key start                                | Last login                    
-----           | --------------       | -----           | ---- | -------------        | ---------                                | ----------                    
u987891158      | /home/u987891158     | /bin/bash       | 1    | ecdsa-sha2-nistp521  | AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlz | Feb 20 22:17 - 
```
