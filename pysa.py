#!/usr/bin/env python
#
# Copyright (©) 2015 Marcel Ribeiro Dantas
#
# mribeirodantas at fedoraproject.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


def bubble_sort(l, optimized=False):
    ''' Bubble sort, sometimes referred to as sinking sort, is a simple sorting
    algorithm that repeatedly steps through the list to be sorted, compares
    each pair of adjacent items and swaps them if they are in the wrong order.
    The pass through the list is repeated until no swaps are needed, which
    indicates that the list is sorted. The algorithm, which is a comparison
    sort, is named for the way smaller elements "bubble" to the top of the
    list. Although the algorithm is simple, it is too slow and impractical for
    most problems even when compared to insertion sort.'''

    n = len(l)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if l[i-1] > l[i]:
                l[i], l[i-1] = l[i-1], l[i]
                swapped = True
        if optimized:  # slightly optimized version
            n -= 1
    return l


def gnome_sort(l):
    ''' Gnome sort (or Stupid sort) is a sorting algorithm originally proposed
    by Dr. Hamid Sarbazi-Azad (Professor of Computer Engineering at Sharif
    University of Technology) in 2000 and called stupid sort[1] (not to be
    confused with bogosort), and then later on described by Dick Grune and named
    "gnome sort" from the observation that it is "how a gnome sorts a line of
    flower pots.'''

    pos = 1
    while pos < len(l):
        if l[pos] >= l[pos-1]:
            pos += 1
        else:
            l[pos], l[pos-1] = l[pos-1], l[pos]
            if pos > 1:
                pos -= 1
    return l


def cocktail_sort(l):
    '''Cocktail sort, also known as bidirectional bubble sort, cocktail shaker
    sort, shaker sort (which can also refer to a variant of selection sort),
    ripple sort, shuffle sort,[1] or shuttle sort, is a variation of bubble
    sort that is both a stable sorting algorithm and a comparison sort. The
    algorithm differs from a bubble sort in that it sorts in both directions on
    each pass through the list.'''

    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(l)-2):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
        if swapped is False:
            break

        swapped = False
        for i in range(len(l)-2, -1, -1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True

    return l

print cocktail_sort([1, 10, 2, 25, 22, 30, 100])
