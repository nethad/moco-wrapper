from .. import IntegrationTest

from moco_wrapper.util.response import JsonResponse, ListingResponse, EmptyResponse
from datetime import date
import random

class TestUserPresence(IntegrationTest):
    def get_user(self):
        with self.recorder.use_cassette("TestUserPresence.get_user"):
            user = self.moco.User.getlist().items[0]
            return user

    def test_create(self):
        with self.recorder.use_cassette("TestUserPresence.test_create"):
            pre_date = self.create_random_date()
            from_time  = "08:30"
            to_time = "10:30"

            pre_create = self.moco.UserPresence.create(pre_date, from_time, to_time)

            assert pre_create.response.status_code == 200
            
            assert isinstance(pre_create, JsonResponse)
            
            assert pre_create.data.date is not None
            assert pre_create.data.from_time == from_time
            assert pre_create.data.to_time == to_time

    def test_get(self):
        with self.recorder.use_cassette("TestUserPresence.test_get"):
            pre_date = self.create_random_date()
            from_time  = "08:30"
            to_time = "10:30"

            pre_create = self.moco.UserPresence.create(pre_date, from_time, to_time)
            pre_get = self.moco.UserPresence.get(pre_create.data.id)

            assert pre_create.response.status_code == 200
            assert pre_get.response.status_code == 200

            assert isinstance(pre_create, JsonResponse)
            assert isinstance(pre_get, JsonResponse)
            
            assert pre_get.data.date is not None
            assert pre_get.data.from_time == from_time
            assert pre_get.data.to_time == to_time

    def test_getlist(self):
        user = self.get_user()

        with self.recorder.use_cassette("TestUserPresence.test_getlist"):
            pre_list = self.moco.UserPresence.getlist(
                from_date=date(2020, 1, 1),
                to_date=date(2021, 1, 1),
                user_id=user.id
            )

            assert pre_list.response.status_code == 200

            assert isinstance(pre_list, ListingResponse)

    def test_update(self):
        with self.recorder.use_cassette("TestUserPresence.test_update"):
            pre_create = self.moco.UserPresence.create(
                self.create_random_date(),
                "10:30",
                "14:00"
            )

            pre_date = self.create_random_date()
            from_time = "08:00"
            to_time = "09:30"

            pre_update = self.moco.UserPresence.update(
                pre_create.data.id,
                pres_date=pre_date,
                from_time=from_time,
                to_time=to_time,
            )

            assert pre_create.response.status_code == 200
            assert pre_update.response.status_code == 200

            assert isinstance(pre_create, JsonResponse)
            assert isinstance(pre_update, JsonResponse)

            assert pre_update.data.date is not None
            assert pre_update.data.from_time == from_time
            assert pre_update.data.to_time == to_time


    def test_delete(self):
        with self.recorder.use_cassette("TestUserPresence.test_delete"):
            pre_create = self.moco.UserPresence.create(
                self.create_random_date(),
                "10:00",
                "11:00"
            )

            pre_delete = self.moco.UserPresence.delete(pre_create.data.id)

            assert pre_create.response.status_code == 200
            assert pre_delete.response.status_code == 204

            assert isinstance(pre_create, JsonResponse)
            assert isinstance(pre_delete, EmptyResponse)

    def test_touch(self):
        with self.recorder.use_cassette("TestUserPresence.test_touch"):
            pre_touch = self.moco.UserPresence.touch()

            #touch it a second time to discard it
            pre_sec_touch = self.moco.UserPresence.touch()

            assert pre_touch.response.status_code == 200
            
            assert isinstance(pre_touch, EmptyResponse)