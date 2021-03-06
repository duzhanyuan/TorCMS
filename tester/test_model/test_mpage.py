# -*- coding:utf-8 -*-

from torcms.core import tools
from torcms.model.wiki_model import MWiki
import tornado.escape


class TestMWiki():
    def setup(self):
        print('setup 方法执行于本类中每条用例之前')
        self.uu = MWiki()
        self.raw_count = self.uu.get_counts()
        self.page_slug = 'aaa'
        self.uid = tools.get_uuid()

    def test_insert(self):
        raw_count = self.uu.get_counts()
        post_data = {
            'title': 'title',
            'slug': 'sadfsadf',
            'id_user': 'Tome',
            'cnt_md': '## adslkfjasdf\n lasdfkjsadf',
            'view_count': 1,

        }
        self.uu.create_page('sadfsadf', post_data)
        new_count = self.uu.get_counts()

        tt = self.uu.get_by_uid(self.page_slug)

        # assert tt.title == post_data['title'][0]
        # assert tt.cnt_md == tornado.escape.xhtml_unescape(post_data['cnt_md'][0])
        # assert raw_count + 1 == new_count

        self.tearDown()

    def test_insert_2(self):
        '''Wiki insert: Test invalid title'''
        post_data = {
            'title': '',
            'id_user': 'Tome',
            'cnt_md': '## adslkfjasdf\n lasdfkjsadf',
            'view_count': 1,
        }
        uu = self.uu.create_page('abcd', post_data)
        assert uu == False

        post_data = {
            'title': '1',
            'id_user': 'Tome',
            'cnt_md': '## adslkfjasdf\n lasdfkjsadf',
            'view_count': 1,
        }
        uu = self.uu.create_page('bdef', post_data)
        assert uu == False

        post_data = {
            'title': '天',
            'id_user': 'Tome',
            'cnt_md': '## adslkfjasdf\n lasdfkjsadf',
            'view_count': 1,
        }
        uu = self.uu.create_page('aaaa', post_data)
        assert uu == False
        self.tearDown()

    def test_query_all(self):
        self.uu.query_all()
        assert True
        self.tearDown()

    def test_get_by_slug(self):
        self.uu.get_by_uid('aa')
        assert True
        self.tearDown()

    def test_update_cnt(self):
        post_data = {
            'user_name': 'name',
            'cnt_md': '## adslkfjasdf\n lasdfkjsadf',

        }
        self.uu.update_cnt(self.uid, post_data)
        assert True
        self.tearDown()

    def test_update(self):
        post_data = {
            'title': 'title',
            'user_name': 'Tome',
            'cnt_md': '## adslkfjasdf\n lasdfkjsadf',
        }
        self.uu.update(self.uid, post_data)
        assert True
        self.tearDown()

    def test_query_recent_edited(self):
        timstamp = tools.timestamp()
        self.uu.query_recent_edited(timstamp)
        assert True
        self.tearDown()

    def tearDown(self):
        print("function teardown")
        tt = self.uu.get_by_uid(self.page_slug)
        if tt:
            self.uu.delete(tt.uid)
