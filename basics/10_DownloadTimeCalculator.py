# coding: utf-8

# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

data_sizes = {
    'kb': 2 ** 10,
    'kB': 2 ** 10 * 8,
    'Mb': 2 ** 20,
    'MB': 2 ** 20 * 8,
    'Gb': 2 ** 30,
    'GB': 2 ** 30 * 8,
    'Tb': 2 ** 40,
    'TB': 2 ** 40 * 8
}

import math

def download_time(filesize, fileUnit, BandWidth, BandWiddthUnit):
    filesize *= data_sizes[fileUnit]
    BandWidth *= data_sizes[BandWiddthUnit]
    time = filesize / BandWidth
    seconds = time % 60
    time = math.floor(time/60)
    minutes = time % 60
    time = math.floor(time/60)

    hours = time % 60

    formatted_time = f'{hours} hour{"s" if hours != 1 else ""}, {minutes} minute{"s" if minutes != 1 else ""}, {seconds} second{"s" if seconds != 1 else ""}'
    return formatted_time

print(download_time(1024, 'kB', 1, 'MB'))
# >>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
