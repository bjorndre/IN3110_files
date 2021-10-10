# README.md Assignment2 

## Task 2.1

### Prerequisites

No prerequisites needed

### Functionality

This script moves a directory and/or a file to a different directory.

### Missing Functionality

Can only move one file or directory at a time, can not create new directories.

### Usage

To use the code, you must run the command
```bash
./move.sh src dst
```
Where src is the directory/file that will be moved, and dst is the directory you want to move it too.

## Task 2.2 and 2.3

### Prerequisites

None

### Functionality

This script can be used to track time

### Missing Functionality

Can only have one tracker active at once. I don't think it works if tracking on new years eve, so spend that time watching fireworks instead

### Usage

To use the code, you can either run the command with
```bash
./track.sh
```
or better, source the function using
```bash
source track.sh
```
which will let you use the track function even outside the directory where it's stored.

if sourced, you can run the function with
```bash
track
```

For the function to work you need to send in a command

```bash
track start [label]
```
will start a time tracking labeled label

```bash
track stop
```
will stop the current time tracker

```bash
track status
```
will tell you what time tracker is currently running

```bash
track log
```
will give you a log off all the time trackers, and how much time each of them took.