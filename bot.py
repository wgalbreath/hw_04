from re import sub
import praw
import prawcore
import random
import datetime
import time
from textblob import TextBlob


# FIXME:
# copy your generate_comment function from the madlibs assignment here
myMadlibs = [
    "The government has [MANY] [WORKERS]. Within it, there are [MANY] [BRANCHES]. Each [WORKER] specializes in a [PARTICULAR] subject area to make or fix laws within it.",
    "The government [WORKERS] have [A LOT OF] [RESPONSIBILITIES]. They must [TAKE CARE OF] each [CITIZEN] and [LISTEN] to their needs.",
    "The politician [MUST] pitch to the [PEOPLE OF AMERICA] to be reelected each term. If they do not campaign, then they will [LOSE]. [THUS], it is in their [FAVOR] to campaign. ",
    "In order to get the [HIGHEST] number of votes from [PEOPLE OF AMERICA], the politicians [MUST] [PERSUADE] the voters. Each American has [ONE] vote to cast. They will then go up to the ballot and make their [SELECTION].",
    "There are [MANY] examples of [PAST] [REPUBLICAN] presidents, [INCLUDING] Hoover, Coolidge, [TRUMP] and more. They all served as president for [AT LEAST] [FOUR YEARS].",
    "Past [DEMOCRATIC] presidents include [WILSON], [CARTER], [CLINTON], and more. Each of those presidents also served for [AT LEAST] [FOUR YEARS].",
]

myReplacement = {
    'MANY' : ['many', 'several', 'countless', 'a lot of', 'lots of', 'a whole lot of'],
    'WORKERS' : ['workers', 'employees'],
    'BRANCHES' : ['branches', 'sectors', 'departments'],
    'WORKER' : ['worker', 'employee'],
    'PARTICULAR'  : ['particular', 'specific'],
    'A LOT OF' : ['a lot of', 'many', 'several', 'countless', 'lots of', 'a whole lot of'],
    'RESPONSIBILITIES' : ['responsibilities', 'duties', 'tasks'],
    'TAKE CARE OF' : ['take care of', 'protect', 'help'],
    'MUST' : ['must', 'needs to', 'should'],
    'PEOPLE OF AMERICA' : ['people of America', 'Americans', 'US citizens'],
    'CITIZEN' : ['citizen', 'person in America', 'US citizen', 'American'],
    'LISTEN' : ['listen', 'understand', 'hear', 'respond'],
    'LOSE' : ['lose', 'not win'],
    'THUS' : ['Thus', 'Therefore', 'Consequently', 'So'],
    'FAVOR' : ['favor', 'best interest'],
    'HIGHEST' : ['highest', 'greatest', 'largest'],
    'PERSUADE' : ['persuade', 'convince'],
    'ONE' : ['one', '1', 'a single'],
    'SELECTION' : ['selection', 'choice', 'decision'],
    'PAST' : ['past', 'historic', 'previous'],
    'REPUBLICAN' : ['Republican', 'right-winged', 'red-party'],
    'INCLUDING' : ['including', 'such as', 'for instance,'],
    'FAVOR' : ['favor', 'best interest'],
    'TRUMP' : ['Trump', 'Nixon', 'Ford'],
    'AT LEAST' : ['at least', 'a minimum of'],
    'TRUMP' : ['Trump', 'Nixon', 'Ford'],
    'DEMOCRATIC' : ['Democratic', 'left-winged', 'blue-party'],
    'WILSON' : ['Wilson', 'Obama'],
    'CARTER' : ['Carter', 'Nixon'],
    'CLINTON' : ['Clinton', 'Truman', 'Harding', 'Taft'],
    'FOUR YEARS' : ['four years', '4 years', '47 months', '1461 days'],
}

def generate_comment():
    g = random.choice(myMadlibs)
    for k in myReplacement.keys():
        g = g.replace('['+k+']', random.choice(myReplacement[k])) # '['+k+']' makes sure that only the things surrounded by brackets can be replaces
    return g

# FIXME: DONE
# connect to reddit 
reddit = praw.Reddit('bot')

# FIXME: DONE
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
# submission_url = 'https://old.reddit.com/r/BotTown/comments/qzw1eg/mcdonald_check_here/'
# submission_url = 'https://old.reddit.com/r/BotTown/comments/qvlbmk/test_submission_for_lecture_bots/?'
# submission_url = 'https://old.reddit.com/r/BotTown/comments/r05c2s/bmacdonalds_assignment_page/?'
submission_url = 'https://old.reddit.com/r/BotTownFriends/comments/r1ie4e/heres_bmacs_post/?'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True: # change this back to a while loop for final submission (using an if statement makes it cleaner in the terminal for now)

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None) # uncomment this for the final submisison; this clicks the "load more comments" button on Reddit, giving you all commments (but it can load the program slowly b/c the limit is None)
    # all_comments = [] # having this line is optional
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = [] # using an accumulator 
    for comment in all_comments: # want to remove my comments b/c you can't reply to your own comment
        # print('comment.author=', comment.author)
        # print('authortype', type(comment.author))
        if str(comment.author) != 'BotMacDonald':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text) # replying to a submission (not a comment)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = [] # making a copy of not_my_comments 
        # submission.comments.replace_more(limit=None)
        for comment in not_my_comments:
            replied = False
            for reply in comment.replies:
                if str(reply.author) == 'BotMacDonald':
                    replied = True
            if replied == False:
                comments_without_replies.append(comment)


            #     commentReplyAuthor.append(str(reply.author))
            # if commentReplyAuthor == 'BotMacDonald':
            #     pass
            # else:
            #     comments_without_replies.append(comment)
            #####
            # me = False
            # for reply_of_a in comment.replies.list():
            #     if str(comment.author) == 'BotMacDonald':
            #         me = True
            # if me == False:
            #     comments_without_replies.append(comment)
        # print('comments_without_replies=', comments_without_replies)
    #3) when to use try/except vs fixing the error? IS THE ERROR MY FAULT (keyerror, indexerror) OR SOMEONE ELSE (if error from praw, APIexception)?

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        ########### old code when I wasn't doing the Extra Credit:
        # if len(comments_without_replies) > 0:
        #     comment = random.choice(comments_without_replies)
        #     print('here=', comment)
        #     print('comment.replies-', len(comment.replies))
        #     for i in comment:
        #         print('i=', i)
        #         if i.reply.author != 'BotMacDonald':
        #             print('i.author=', i.author)
    
        if len(comments_without_replies) > 0:
            try:
                sortedComment = sorted(comments_without_replies, key=lambda comment: comment.score, reverse=True)[0]
                # print('sortedComment_2 = ', sortedComment)
                
                # top_comment = sortedComment[0]
                # print('top comment = ', top_comment)

                #print('submission.reply(generate_comment())=', submission.reply(generate_comment())) # can delete this 
                #sortedComment.reply(generate_comment())
                # for a in sortedComment:
                #     a.reply(generate_comment())
                sortedComment.reply(generate_comment())
            except praw.exceptions.APIException:
                pass
            except prawcore.exceptions.BadRequest:
                pass
            except prawcore.exceptions.RequestException:
                pass
            time.sleep(1)

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    # ADD_THE_RIGHT_THING_HERE = 'https://old.reddit.com/r/BotTown/' ### DELETE THIS LIKE AFTER I FIX THE BELOW
    # submission = random.choice( ADD_THE_RIGHT_THING_HERE )

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.

    
    submission_url = reddit.subreddit("BotTownFriends")
    x = list(submission_url.hot(limit=5))
    submission = random.choice(x)
    print("random submission.title=", submission.title)
    time.sleep(1)
    # DevOps = Developer Operations 
    
    
    ###########################################################################################
    
    # Extra Credit 6.
    
    # for submission in reddit.subreddit("BotTown/top").top(limit=None):
    #     submission.comment().comments.top("all time")
    #     responded = False
    #     try:
    #         if str(comment.author) == 'BotMacDonald':
    #             responded = True
    #             break
    #         elif responded == False:
    #                 comments_without_replies.append(comment)
    #     except prawcore.exceptions.BadRequest:
    #         pass
    

    # Extra Credit 7.
    # for comment in not_my_comments:
    #     if 'joe' in comment.body or 'Joe' in comment.body or 'biden' in comment.body or 'Biden' in comment.body:
    #         comment.upvote()
    #         print('a comment was just upvoted')
    # for submission in reddit.subreddit("BotTown").hot(limit=5):
    #     if 'joe' in submission.title or 'Joe' in submission.title or 'biden' in submission.title or 'Biden' in submission.title:
    #         submission.upvote()
    #         print('submission=', submission.title) # this is not working correctly bc it says it is upvoting things when the title is "Cat."
    #         print('a submission was just upvoted')
    


    # Extra Credit 7.5 (for 7 and 7.5)
    numupvoted = 0
    numdownvoted = 0
    numupvotedReplies = 0
    numdownvotedReplies = 0
    for comment in not_my_comments: 
        text = TextBlob(str(comment.body.lower()))
        polarity = text.sentiment.polarity
        if 'joe' in comment.body.lower() or 'biden' in comment.body.lower():
            if polarity < 0:
                comment.downvote()
                # print('comment downvoted')
                numdownvoted += 1
                # print('numdownvoted:', numdownvoted)
            elif polarity >= 0:
                comment.upvote()
                # print('comment upvoted')
                numupvoted += 1
                # print('numupvoted:', numupvoted)
            submissionCombo = numupvoted + numdownvoted
            print('submissionCombo:', submissionCombo)
        else: 
            pass  
        for reply in comment.replies:
            if 'joe' in comment.body.lower() or 'biden' in comment.body.lower():
                if polarity > 0:
                    comment.upvote()
                    # print('comment upvoted')
                    numupvotedReplies += 1
                    # print('REPLIES numupvoted:', numupvotedReplies)
                elif polarity <= 0:
                    comment.downvote()
                    # print('comment downvoted')
                    numdownvotedReplies += 1
                    # print('REPLIES numdownvoted:', numdownvotedReplies)
            repliesCombo = numupvotedReplies + numdownvotedReplies
            print('commentsCombo =', repliesCombo)
        else: 
            pass  
    
    
    '''
    goodphrase = 'joe' or 'Joe' or 'biden' or 'Biden'
    numupvoted = 0
    numdownvoted = 0
    numupvotedReplies = 0
    numdownvotedReplies = 0
    subRed = reddit.subreddit("BotTownFriends").hot(limit=5)
    for post in subRed: # this is for SUBMISSIONS
        print('post=',post.title)
        # tone = blob.sentiment.polarity
        if goodphrase in post.title:
            subcontent = TextBlob(str(post.title))   
            print('goodphrase printed=', goodphrase)
            if subcontent.sentiment.polarity > 0:
                post.upvote()
                numupvoted += 1
                # print('postVOTED=', post.title)
                print('numupvoted:', numupvoted)
            elif subcontent.sentiment.polarity <= 0:
                post.downvote()
                numdownvoted += 1
                print('numdownvoted:', numdownvoted)
            submissionCombo = numupvoted + numdownvoted
        for reply in post.comments.list(): # this is for REPLIES
            text = TextBlob(str(reply.body))  
            if goodphrase in reply.body:
                if text.sentiment.polarity > 0:
                    reply.upvote()
                    numupvotedReplies += 1
                elif text.sentiment.polarity <= 0:
                    reply.downvote()
                    numdownvotedReplies += 1
            repliesCombo = numupvotedReplies + numdownvotedReplies
            print('repliesCombo =', repliesCombo)
            for comments in list(reply.replies): # this is for top level comments TLC
                text2 = TextBlob(str(comments.body))  
                if goodphrase in comments.body:
                    if text2.sentiment.polarity > 0:
                        comments.upvote()
                        numupvotedReplies += 1
                    elif text2.sentiment.polarity <= 0:
                        comments.downvote()
                        numdownvotedReplies += 1
            commentCombo = numupvotedReplies + numdownvotedReplies
            print('commentCombo =', commentCombo)
            totalCommentsVotes = commentCombo + repliesCombo
            print('totalCommentsVotes=', totalCommentsVotes)
            
    # print('submissionCombo =', submissionCombo)
    '''
    '''
    for comment in not_my_comments:
        blob = TextBlob(str(comment.body))
        tone = blob.sentiment.polarity
        try:
            if 'joe' in comment.body or 'Joe' in comment.body or 'biden' in comment.body or 'Biden' in comment.body:
                if tone > 0: 
                    comment.upvote()
                    numupvoted += 1
                # print('comment numupvoted count =', numupvoted)
                elif tone <= 0:
                    comment.downvote()
                    numdownvoted += 1
                # print('comment numdownvoted count =', numdownvoted)
                commentCombo = numupvoted + numdownvoted
                print('commentCombo =', commentCombo)
            else:
                pass
        except prawcore.exceptions.NotFound:
            pass
        
        #
        for reply in comment.replies: #running the same loop for replies
            # blob = TextBlob(str(comment.body))
            # tone = blob.sentiment.polarity
            try:
                if 'joe' in reply.body or 'Joe' in reply.body or 'biden' in reply.body or 'Biden' in reply.body:
                    if tone > 0: 
                        comment.upvote()
                        numupvoted += 1
                    # print('comment numupvoted count =', numupvoted)
                    elif tone <= 0:
                        comment.downvote()
                        numdownvoted += 1
                    # print('comment numdownvoted count =', numdownvoted)
                    commentCombo = numupvoted + numdownvoted
                    print('commentCombo with replies =', commentCombo)
                else:
                    pass
            except prawcore.exceptions.NotFound:
                pass
    
    for submission in reddit.subreddit("BotTownFriends").hot(limit=None):
        blob = TextBlob(str(submission.title))
        tone = blob.sentiment.polarity
        try:
            if 'joe' in submission.title or 'Joe' in submission.title or 'biden' in submission.title or 'Biden' in submission.title:
                if tone > 0:
                    submission.upvote()
                    numupvoted += 1
                    # print('submissions numupvoted count =', numupvoted)
                    # print("this was upvoted for tone", submission)
                elif tone <= 0:
                    submission.downvote()
                    numdownvoted += 1
                    # print('submissions numdownvoted count =', numdownvoted)
                    submissionCombo = numupvoted + numdownvoted 
                    print('submissionCombo =', submissionCombo)
        #         print("this was downvoted for tone", submission)
            else:
                pass   
        except prawcore.exceptions.Forbidden:
            pass
            # print("this had no tone", submission)
        '''
    

# QUESTIONS
# how to get valid comments?
# 6.?? -- look at task 4