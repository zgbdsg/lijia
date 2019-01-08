#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'todo.Index',
    '/main',                    pre_fix + 'todo.Main',
    '/admin',                    pre_fix + 'todo.Admin',
    '/login',                    pre_fix + 'todo.Login',
    '/logout',                    pre_fix + 'todo.Logout',
    '/manage',                    pre_fix + 'todo.Manage',
    '/manage/update-video-data',                    pre_fix + 'todo.Update_video_data',
    '/todo/new',            pre_fix + 'todo.New',
    '/todo/(\d+)',          pre_fix + 'todo.View',
    '/todo/(\d+)/edit',     pre_fix + 'todo.Edit',
    '/todo/(\d+)/delete',   pre_fix + 'todo.Delete',
    '/user/(\d+)/delete',   pre_fix + 'todo.DelUser',
    '/todo/(\d+)/finish',   pre_fix + 'todo.Finish',
    '/AddUser',             pre_fix + 'todo.AddUser',
    '/AddUsers',             pre_fix + 'todo.AddUsers',
    '/Admin',               pre_fix + 'todo.Admin',
    '/Login',               pre_fix + 'todo.Login',
    '/sign/(\d+)',          pre_fix + 'todo.Sign',
    '/sign/(\d+)/read',          pre_fix + 'todo.Sign_read',
    '/sign/(\d+)/score',          pre_fix + 'todo.Score',
    '/sign/(\d+)/action',          pre_fix + 'todo.Action',
    '/sign/(\d+)/insert-play-data',          pre_fix + 'todo.Insert_play_data',
    '/sign/(\d+)/insert-question-data',          pre_fix + 'todo.Insert_question_data',
    '/sign/(\d+)/select-play-data',          pre_fix + 'todo.Select_play_data',
    '/sign/(\d+)/select-index-data',          pre_fix + 'todo.Select_index_data',
    '/sign/(\d+)/select-question-index-data',          pre_fix + 'todo.Select_question_index_data',
    '/sign/(\d+)/Insert-answer-data',          pre_fix + 'todo.Insert_answer_data',

)
