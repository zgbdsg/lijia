#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from datetime import datetime
import random
import sys
import json
import os

reload(sys)
sys.setdefaultencoding('utf-8')

render = settings.render
db = settings.db
tb = 'todo'
user = 'user'
video = 'video'
score = 'score'
action = 'action'
playdb = 'play'
questiondb = 'question'
answerdb = 'answer'

session = web.config._session


def get_by_id(id):
    s = db.select(video, where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]


def get_plays_by_id(id):
    s = db.select(playdb, where='vid=$id', vars=locals())
    if not s:
        return False
    return s


def get_questions_by_id(id, btnId):
    s = db.select(questiondb, where='vid=$id and btnId=$btnId', vars=locals())
    if not s:
        return False
    return s


def get_user_by_name(name):
    s = db.select(user, where='name=$name', vars=locals())
    if not s:
        return False
    return s[0]

def get_user_by_id(id):
    s = db.select(user, where='id=$id', vars=locals())
    if not s:
        return ''
    return s[0]

class New:

    def POST(self):
        x = web.input(fileUpload={})
        print x.keys()
        title = x['title']
        f = x['fileUpload']
        t = x['type']
        print t

        print f.filename
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0, 100)
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum);
        uniqueNum = str(nowTime) + str(randomNum);
        tempf = open('static/video/%s.mp4' % uniqueNum, 'wb')
        tempf.write(f.value)
        tempf.close()

        if not title:
            return render.error('标题是必须的', None)
        db.insert(video, type=t, name=title, path='/static/video/%s.mp4' % uniqueNum, isExp=0)
        raise web.seeother('/admin')


class Finish:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        status = i.get('status', 'yes')
        if status == 'yes':
            finished = 1
        elif status == 'no':
            finished = 0
        else:
            return render.error('您发起了一个不允许的请求', '/')
        db.update(tb, finished=finished, where='id=$id', vars=locals())
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        return render.todo.edit(todo)

    def POST(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        title = i['title']
        if not title:
            return render.error('标题是必须的', None)
        db.update(tb, title=title, where='id=$id', vars=locals())
        return render.error('修改成功！', '/')


class Delete:

    def GET(self, id):
        v = get_by_id(id)
        if not v:
            return render.error('没找到这条记录', None)

        print v['path']
        os.remove('./%s' % v['path'])
        db.delete(video, where='id=$id', vars=locals())
        db.delete(playdb, where='vid=$id', vars=locals())
        return render.error('删除成功！', '/admin')


class Index:

    def GET(self):
        if session.get('logged_in', False):
            videos1 = db.select(video, where='type=1', order='id asc')
            videos2 = db.select(video, where='type=2', order='id asc')
            videos3 = db.select(video, where='type=3', order='id asc')
            videos4 = db.select(video, where='type=4', order='id asc')

            return render.index(videos1, videos2, videos3, videos4)
        else:
            raise web.seeother('/login')


class Main:

    def GET(self):
        if session.get('logged_in', False):
            videos = db.select(video, where='isExp=1', order='ind asc')
            videos = list(videos)
            for v in videos:
                print(v)
            return render.main(videos)
        else:
            raise web.seeother('/login')


class Sign:

    def GET(self, id):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        if not session.get('admin', False):
            raise web.seeother('/')
        v = get_by_id(id)
        return render.sign(v)


class Sign_read:

    def GET(self, id):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        v = get_by_id(id)
        return render.sign_read(v)


class Insert_play_data:
    def POST(self, id):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        if not session.get('admin', False):
            raise web.seeother('/')
        play = web.input()

        vid = int(id)
        t = int(play['type'])
        length = int(play['length'])
        time = float(play['time'])
        title = play['title']
        url = play['url'][7:]
        desc = play['desc']
        topY = play['topY'][:-1]
        leftX = play['leftX'][:-1]
        print topY, leftX
        result = db.insert(playdb, vid=vid, type=t, length=length,
                           time=time, title=title, url=url, des=desc,
                           topY=topY, leftX=leftX)
        if result:
            return json.dumps(True)
        else:
            return json.dumps(False)


class Insert_question_data:
    def POST(self, id):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        if not session.get('admin', False):
            raise web.seeother('/')
        play = web.input()
        print(play.keys())
        vid = int(id)
        t = int(play['type'])
        length = int(play['length'])
        time = float(play['time'])
        title = play['title']
        url = play['url'][7:]
        desc = play['desc']
        topY = play['topY'][:-1]
        leftX = play['leftX'][:-1]
        questions = json.loads(play["questions"])
        question = {}
        for i in range(1, 11):
            tem = str(i)
            if i <= len(questions):
                question[tem] = json.dumps(questions[i-1])
            else:
                question[tem] = ""
        result = db.insert(playdb, vid=vid, type=t, length=length,
                           time=time, title=title, url=url, des=desc,
                           topY=topY, leftX=leftX)
        print(result)
        result1 = db.insert(questiondb, vid=vid, btnId=result, Q1=question["1"],
                            Q2=question["2"], Q3=question["3"], Q4=question["4"],
                            Q5=question["5"], Q6=question["6"], Q7=question["7"],
                            Q8=question["8"], Q9=question["9"], Q10=question["10"])
        print(result1)
        if result1:
            return json.dumps(True)
        else:
            return json.dumps(False)


class Select_play_data:
    def POST(self, id):
        plays = get_plays_by_id(id)
        if not plays:
            return json.dumps([])

        plays = list(plays)
        for p in plays:
            p['topY'] = '%.14f%%' % float(p['topY'])
            p['leftX'] = '%.14f%%' % float(p['leftX'])
            p['url'] = 'http://%s' % p['url']
            p['desc'] = p['des']

        result = json.dumps(plays)
        print result
        if plays:
            return json.dumps(plays)
        else:
            return json.dumps([])


class Select_question_index_data:
    def POST(self, id):
        plays = get_plays_by_id(id)
        parm = web.input()
        print parm
        ind = int(parm['index'])
        btnId = parm['btnId']
        questions = get_questions_by_id(id, btnId)
        print questions
        if not plays:
            return json.dumps([])
        plays = list(plays)
        p = plays[ind]
        # for p in plays:
        p['topY'] = '%.14f%%' % float(p['topY'])
        p['leftX'] = '%.14f%%' % float(p['leftX'])
        p['url'] = 'http://%s' % p['url']
        p['desc'] = p['des']
        if questions:
            size = 0
            target = list(questions)[0]
            for i in xrange(10):
                if len(target["Q%d"%(i + 1)]) > 0 :
                    size += 1
                else:
                    target["size"] = size
                    break
            p['question'] = json.dumps(target)
        else:
            p['question'] = json.dumps([])
        print p
        result = json.dumps(p)
        if plays:
            return result
        else:
            return json.dumps([])

class Select_index_data:
    def POST(self, id):
        plays = get_plays_by_id(id)
        parm = web.input()
        print parm
        ind = int(parm['index'])
        if not plays:
            return json.dumps([])
        plays = list(plays)
        p = plays[ind]
        # for p in plays:
        p['topY'] = '%.14f%%' % float(p['topY'])
        p['leftX'] = '%.14f%%' % float(p['leftX'])
        p['url'] = 'http://%s' % p['url']
        p['desc'] = p['des']
        print p
        result = json.dumps(p)
        if plays:
            return result
        else:
            return json.dumps([])



class Insert_answer_data:
    def POST(self, id):
        parm = web.input()
        print parm
        vid = int(id)
        btnId = parm['btnId']
        uid = session.get('uid', 0)
        ans = json.loads(parm["ans"])
        print ans
        result = db.insert(answerdb, uid=uid, vid=vid, btnId=btnId, a2Q1=json.dumps(ans["Q1"]),
                   a2Q2=json.dumps(ans["Q2"]), a2Q3=json.dumps(ans["Q3"]), a2Q4=json.dumps(ans["Q4"]),
                   a2Q5=json.dumps(ans["Q5"]), a2Q6=json.dumps(ans["Q6"]), a2Q7=json.dumps(ans["Q7"]),
                   a2Q8=json.dumps(ans["Q8"]), a2Q9=json.dumps(ans["Q9"]), a2Q10=json.dumps(ans["Q10"]))
        if result:
            return json.dumps(True)
        else:
            return json.dumps(False)

class Clear:
    def POST(self, id):
        db.delete(playdb, where='vid=$id', vars=locals())
        return render.error('删除成功！', '/sign')


class AddUser:

    def GET(self):
        pass

    def POST(self):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        i = web.input()
        username = i.get('username')
        pwd = i.get('pwd')
        result = get_user_by_name(username)
        if not result:
            db.insert(user, name=username, pwd=pwd, admin='0')
        raise web.seeother('/manage')


class AddUsers:

    def GET(self):
        pass

    def POST(self):
        x = web.input()
        f = x['userfile']
        print(f)
        userlist = f.split("\n")
        userlist = [a.strip() for a in userlist]
        print(userlist)

        print(len(userlist))
        if len(userlist) > 0:
            db.delete(user, where='admin=0', vars=locals())
        for item in userlist:
            temp = item.split(",")
            print(temp[0], temp[1], temp[2])
            db.insert(user, name=temp[0], pwd=temp[1], admin=temp[2]);
        raise web.seeother('/manage')


class DelUser:

    def GET(self, id):
        u = get_user_by_id(id)
        if not u:
            return render.error('wrong user', '/manage')

        print("delete id %s"%id)
        db.delete(user, where='id=$id', vars=locals())
        return render.error('delete success', '/manage')

    def POST(self):
        pass


class Logout:

    def GET(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        value = "Logout"
        if session.get('uid', 0) > 0:
            result = db.insert(action, vid=0, uid=session.uid, bid=0, timestamp=timestamp,
                               action=value)
        session.kill()
        return render.login()


class Login:

    def GET(self):
        return render.login()
        pass

    def POST(self):
        i = web.input()
        username = i.get('username')
        passwd = i.get('passwd')
        print username, passwd

        result = get_user_by_name(username)
        print result and result['pwd'] == passwd
        if result and result['pwd'] == passwd:
            print "Login success"
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            value = "Login success"
            db.insert(action, vid=0, uid=result['id'], bid=0, timestamp=timestamp,
                           action=value)

            session.uid = result['id']
            session.logged_in = True
            session.admin = False
            print session.get('logged_in', False)
            print session.get('admin', False)

            web.setcookie('userid', result['id'], 60)
            if result['admin'] == u'1':
                session.admin = True
                raise web.seeother('/admin')
            else:
                raise web.seeother('/main')
                # raise web.seeother('/')
        else:
            return render.login()


class Score:

    def GET(self):
        pass

    def POST(self, id):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        data = web.input()

        vid = int(id)
        uid = session.get('uid', 0)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        value = float(data['score'])
        result = db.insert(score, vid=vid, uid=uid, timestamp=timestamp,
                           value=value)
        if result:
            return json.dumps(True)
        else:
            return json.dumps(False)

        pass


class Action:

    def GET(self):
        pass

    def POST(self, id):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        data = web.input()
        print data

        vid = int(id)
        uid = session.get('uid', 0)

        bid = 0
        if "bid" in data:
            bid = data['bid']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        value = data['action']
        result = db.insert(action, vid=vid, uid=uid, bid=bid, timestamp=timestamp,
                           action=value)
        if result:
            return json.dumps(True)
        else:
            return json.dumps(False)

        pass


class Admin:

    def GET(self):
        print session.get('logged_in', False)
        print session.get('admin', False)
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        if not session.get('admin', False):
            raise web.seeother('/')

        videos1 = db.select(video, where='type=1', order='id asc')
        videos2 = db.select(video, where='type=2', order='id asc')
        videos3 = db.select(video, where='type=3', order='id asc')
        videos4 = db.select(video, where='type=4', order='id asc')

        return render.admin(videos1, videos2, videos3, videos4)
        pass

    def POST(self):
        pass


class Manage:

    def GET(self):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        if not session.get('admin', False):
            raise web.seeother('/')

        users = db.select(user, order='id asc')
        allvideos = db.select(video, order='ind asc')
        return render.manage(users, allvideos)
        pass

    def POST(self):
        pass


class Update_video_data:
    def POST(self):
        if not session.get('logged_in', False):
            raise web.seeother('/login')
        data = web.input()
        vlist = json.loads(data['videoList'])
        print(vlist)
        for item in vlist:
            print(item)
            vid = int(item['id'])
            result = db.update(video, ind=int(item['index']), isExp=int(item['isExp']), where='id=$vid', vars=locals())

        return json.dumps(True)
