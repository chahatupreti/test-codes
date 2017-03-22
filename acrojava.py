# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:28:21 2016

@author: chahat
"""

/**
Method findBestLongForm takes as input a short-form and a longform
candidate (a list of words) and returns the best long-form
that matches the short-form, or null if no match is found.
**/
public String findBestLongForm(String shortForm, String longForm) {
 int sIndex; // The index on the short form
 int lIndex; // The index on the long form
 char currChar; // The current character to match
sIndex = shortForm.length() - 1; // Set sIndex at the end of the
 // short form
lIndex = longForm.length() - 1; // Set lIndex at the end of the
 // long form
for ( ; sIndex >= 0; sIndex--) { // Scan the short form starting
// from end to start
// Store the next character to match. Ignore case
 currChar = Character.toLowerCase(shortForm.charAt(sIndex));
 // ignore non alphanumeric characters
 if (!Character.isLetterOrDigit(currChar))
 continue;
 // Decrease lIndex while current character in the long form
// does not match the current character in the short form.
// If the current character is the first character in the
// short form, decrement lIndex until a matching character
 // is found at the beginning of a word in the long form.
 while (
((lIndex >= 0) &&
(Character.toLowerCase(longForm.charAt(lIndex)) != currChar))
||
 ((sIndex == 0) && (lIndex > 0) &&
(Character.isLetterOrDigit(longForm.charAt(lIndex - 1)))))
 lIndex--;
 // If no match was found in the long form for the current
// character, return null (no match).
if (lIndex < 0)
 return null;
 // A match was found for the current character. Move to the
// next character in the long form.
 lIndex--;
 }
// Find the beginning of the first word (in case the first
 // character matches the beginning of a hyphenated word).
lIndex = longForm.lastIndexOf(" ", lIndex) + 1;
// Return the best long form, the substring of the original
// long form, starting from lIndex up to the end of the original
// long form.
 return 