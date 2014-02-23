blog-planetlabs
===============
A very, very basic blogging site.

Anyone can post blog entries to the site. Anyone can comment on blog posts.

Clicking on an author's name gives a list of posts by that author. 
It's obviously not very realistic, since it would be extremely easy to 
pretend to be someone else, but it demonstrates a little bit of filtering
for the index.

There is also paging in the normal index and in the "posts by author" index
(which share a common template). The main challenge with this was configuring
the urls.

Next steps would definitely be user authentication (for security reasons),
scrolling through lists of posts from the post detail view (next entry/
previous entry), and maybe blog post tags. I wasn't sure how long it would 
take to set up my first Django project from scratch, so I kept it simple.
