# hw_04

Welcome to my homework 4 submission!

The assignment includes several requirements, so I will answer those below:
<br> 
<br> 
<b> a) Clearly states which politician your bot is supporting or opposing. </b>
<br> My madlibs are not about a specific politician, rather it focuses on the general topic of politics. You will will the names of many former presidents in my sentences as well, such as Hoover, Coolidge, Wilson, Obama, and Nixon.


<b> b) Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it. (Below each comment is a button labeled permalink that lets you link to a comment.) </b>
<br> 
[My favorite thread](https://old.reddit.com/r/BotTown/comments/qzzyj0/qanon_shaman_is_sentenced_to_over_3_years_in/) was about 'QAnon Shaman' and then the comments discuss politics. I liked it because it was funny how the conversation starts by discussing the Capitol riot and then the comments just break out into a different conversation. It makes me laugh reading the comments because the bots are "talking" to each other but their conversation is all over the place. Every response is illogiical which makes reading the feed very entertaining.
<br> ![Screen Shot 2021-11-23 at 5 21 04 PM](https://user-images.githubusercontent.com/67754864/143138396-728a26c3-ce13-498e-a18a-b49d72007a7b.png)


<b> c) Includes the output of running the bot_counter.py file on your bot to count how many comments you've created. The output of this command must be inside of a markdown code block (i.e. use the triple backticks notation). </b>
<br> 
```
(base) Williams-MacBook-Air-3:HW_04 williamgalbreath$ python3 bot_counter.py --username=BotMacDonald
len(comments)= 1000
len(top_level_comments)= 801
len(replies)= 199
len(valid_top_level_comments)= 364
len(not_self_replies)= 199
len(valid_replies)= 146
========================================
valid_comments= 510
========================================
```
Plus, here is a screenshot of it:
<br>
![Screen Shot 2021-11-23 at 4 58 50 PM](https://user-images.githubusercontent.com/67754864/143169550-c99c7d4b-647d-4630-9985-9881b74d2d0a.png)


<b> d) Explains what you believe your score should be. Clearly state which tasks you complete/don't complete. </b>
<br> 
My score should be 32/30.
Tasks I completed:
<ul>
  <li> 1. Each task in `bot.py` is worth 3 points. (6 tasks * 3 points/task = 18 points) +18 </li>
  <li> 2. The github repo is worth 2 points. +2 </li>
  <br>
  <li> 1. Getting at least 100 valid comments posted. +2 </li>
  <li> 2. Getting at least 500 valid comments posted. +2 </li>
  <li> 4. Make your bot create new submission posts instead of just new comments. +2 </li>
  <li> 6. Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. +2 </li>
  <li> 7. upvote any comment or submission using TextBlob +4 </li>
  <br>
  In my submissionCombo variable, I added the number of downvotes and upvotes for all submissions. I had over 100 votes on submissions. On the other hand, with my commentsCombo variable, I added the number of downvotes and upvotes for all comments. I reached over 500 votes on comments.
  <br>
  <br>
  <br> Grand total = 32/30


