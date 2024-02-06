#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isSubsequence(char * s, char * t)
{
    size_t sLen = strlen(s);
    size_t tLen = strlen(t);
    size_t i = 0;
    size_t j = 0;
    while (i < sLen && j < tLen)
    {
        if (s[i] == t[j])
        {
            i++;
        }
        j++;
    }
    if (i < sLen)
    {
        return false;
    }
    return true;
}
