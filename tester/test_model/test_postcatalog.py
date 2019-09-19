# -*- coding:utf-8 -*-
from torcms.model.category_model import MCategory
from torcms.core import tools
from torcms.model.post2catalog_model import MPost2Catalog
from torcms.model.post_model import MPost


class TestMCategory():
    def setup(self):
        print('setup 方法执行于本类中每条用例之前')
        self.uid = '0100'
        self.slug = 'slug'

        self.postid = 'greww'

    def test_add_or_update(self):
        post_data = {
            'name': 'category',
            'slug': self.slug,
            'order': '1',
            'kind': '1',
            'pid': 'z100',
        }
        MCategory.add_or_update(self.uid, post_data)
        a = MCategory.get_by_uid(self.uid)
        assert a.pid == post_data['pid']

        post_data2 = {
            'name': 'adsfdsf',
            'pid': 'z222',
            'slug': 'ssskug',

        }
        MCategory.add_or_update(self.uid, post_data2)
        a2 = MCategory.get_by_uid(self.uid)
        assert a2.name == post_data2['name']

    def add_message(self, **kwargs):
        post_data = {
            'name': kwargs.get('name', 'category'),
            'slug': kwargs.get('slug', self.slug),
            'order': kwargs.get('order', '0'),
            'kind': kwargs.get('kind', '1'),
            'pid': kwargs.get('pid', '0000'),
        }
        MCategory.add_or_update(self.uid, post_data)

        p_d = {
            'title': 'iiiii',
            'cnt_md': 'grgr',
            'time_create': '1992',
            'time_update': '1996',
            'user_name': 'yuanyuan',
            'view_count': '1',
            'logo': 'prprprprpr',
            'memo': '',
            'order': '1',
            'keywords': '',
            'extinfo': {},
            'kind': '1',
            'valid': '1',

        }
        i = MPost.get_by_uid(self.postid)
        print(i)

        g = MPost.create_post(self.postid, p_d)
        print(g)

        MPost2Catalog.add_record(self.postid, self.uid)

    def test_update(self):
        post_data = {
            'name': 'adsfdsf',
            'pid': 'z222',

        }
        self.add_message()
        MCategory.update(self.uid, post_data)
        a = MCategory.get_by_uid(self.uid)
        assert a.name == post_data['name']

    def test_update_count(self):
        self.add_message()
        a = MCategory.update_count(self.uid)
        # print(a)
        # assert a==9

    def test_get_by_slug(self):
        self.add_message()

        a = MCategory.get_by_slug(self.slug)
        assert a

    def test_query_field_count(self):
        self.add_message()
        a = MCategory.query_field_count(500)
        print(a.count())

        TF = False
        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True

        assert TF

    def test_query_all(self):
        self.add_message()
        a = MCategory.query_all()
        print(a.count())

        TF = False
        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True
        assert TF

    def test_query_uid_starts_with(self):
        self.add_message()
        a = MCategory.query_uid_starts_with('01')
        TF = False
        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True
        assert TF

    def test_query_pcat(self):
        self.add_message()
        a = MCategory.query_pcat()
        TF = False
        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True
        assert TF

    def test_query_sub_cat(self):
        self.add_message()
        a = MCategory.query_sub_cat('0000')
        TF = False

        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True
        assert TF

    def test_query_kind_cat(self):
        self.add_message()
        a = MCategory.query_kind_cat('1')
        TF = False
        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True
        assert TF

    def test_get_parent_list(self):
        self.add_message()
        a = MCategory.get_parent_list()
        TF = False
        for i in range(a.count()):
            if a[i].uid == self.uid:
                TF = True
        assert TF

    def tearDown(self):
        print("function teardown")
        tt = MCategory.get_by_uid(self.uid)
        if tt:
            MCategory.delete(self.uid)
        tt = MPost.get_by_uid(self.postid)
        if tt:
            MPost.delete(self.postid)
            # a=MPost2Catalog.query_by_post(self.postid)
            # a=MPost2Catalog.query_by_entity_uid(self.postid)
            # print(a.count())
            #
            # MPost2Catalog.del_by_uid(a[0].uid)
        tt = MPost2Catalog.query_by_id(self.uid)
        if tt:
            MPost2Catalog.del_by_uid(self.uid)
            # #出错
