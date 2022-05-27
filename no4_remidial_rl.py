#!/usr/bin/env python
# coding: utf-8

# In[1]:


def naive_justify(text, page_size):
    next = text.get_next()
    total_size = 0
    next_total_size = total_size + next.size()


# In[ ]:


lines = [[next]]
   current_line = 
   


# In[ ]:


while(!text.empty()):
       while(next_total_size < page_size):
           total_size = next_total_size
           next = text.get_next()
           lines[current_line].push(next)
           next_total_size = total_size + next.size()


# In[ ]:


while total_size != page_size:
           add_space(lines[current_line])


# In[ ]:


current_line = current_line + 1


# In[ ]:


def length(word_lengths, i, j):
    return sum(word_lengths[i- 1:j]) + j - i + 1

    return s


# In[ ]:



def break_line(text, L):
    wl = [len(word) for word in text.split()]
    n = len(wl)

    m = dict()
    m[0] = 0


# In[ ]:


m = dict()


# In[ ]:


for i in range(1, n + 1):
    sums = dict()
    k = i
    while (length(wl, k, i) <= L and k > 0):
        sums[(L - length(wl, k, i))**3 + m[k - 1]] = k
        k -= 1
    m[i] = min(sums)
    s[i] = sums[min(sums)]


# In[ ]:


return s

