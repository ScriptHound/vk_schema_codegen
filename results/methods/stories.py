from vkbottle_types.responses import stories, base



class StoriesCategory(BaseCategory):
    async def ban_owner(
        self, owners_ids: List[int], **kwargs
    ) -> base.OkResponseModel:
        """Allows to hide stories from chosen sources from current user's feed.
		:param owners_ids: List of sources IDs
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.banOwner", params)
        model = base.OkResponse
        return model(**response).response

    async def delete(
        self,
		owner_id: Optional[int] = None,
		story_id: Optional[int] = None,
		stories: Optional[List[str]] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """Allows to delete story.
		:param owner_id: Story owner's ID. Current user id is used by default.
		:param story_id: Story ID.
		:param stories: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.delete", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
		owner_id: Optional[int] = None,
		extended: Optional[bool] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> stories.GetResponseModel:
        """Returns stories available for current user.
		:param owner_id: Owner ID.
		:param extended: '1' — to return additional fields for users and communities. Default value is 0.
		:param fields: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.get", params)
        model = stories.GetResponse
        return model(**response).response

    async def get_banned(
        self,
		extended: Optional[bool] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> stories.GetBannedResponseModel:
        """Returns list of sources hidden from current user's feed.
		:param extended: '1' — to return additional fields for users and communities. Default value is 0.
		:param fields: Additional fields to return
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getBanned", params)
        model = stories.GetBannedResponse
        return model(**response).response

    async def get_by_id(
        self,
		stories: List[str],
		extended: Optional[bool] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> stories.GetByIdResponseModel:
        """Returns story by its ID.
		:param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
		:param extended: '1' — to return additional fields for users and communities. Default value is 0.
		:param fields: Additional fields to return
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getById", params)
        model = stories.GetByIdResponse
        return model(**response).response

    async def get_photo_upload_server(
        self,
		add_to_news: Optional[bool] = None,
		user_ids: Optional[List[int]] = None,
		reply_to_story: Optional[str] = None,
		link_text: Optional[str] = None,
		link_url: Optional[str] = None,
		group_id: Optional[int] = None,
		clickable_stickers: Optional[str] = None,
		**kwargs
    ) -> stories.GetPhotoUploadServerResponseModel:
        """Returns URL for uploading a story with photo.
		:param add_to_news: 1 — to add the story to friend's feed.
		:param user_ids: List of users IDs who can see the story.
		:param reply_to_story: ID of the story to reply with the current.
		:param link_text: Link text (for community's stories only).
		:param link_url: Link URL. Internal links on https://vk.com only.
		:param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
		:param clickable_stickers: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getPhotoUploadServer", params)
        model = stories.GetPhotoUploadServerResponse
        return model(**response).response

    async def get_replies(
        self,
		owner_id: int,
		story_id: int,
		access_key: Optional[str] = None,
		extended: Optional[bool] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> stories.GetRepliesResponseModel:
        """Returns replies to the story.
		:param owner_id: Story owner ID.
		:param story_id: Story ID.
		:param access_key: Access key for the private object.
		:param extended: '1' — to return additional fields for users and communities. Default value is 0.
		:param fields: Additional fields to return
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getReplies", params)
        model = stories.GetRepliesResponse
        return model(**response).response

    async def get_stats(
        self, owner_id: int, story_id: int, **kwargs
    ) -> stories.GetStatsResponseModel:
        """Returns stories available for current user.
		:param owner_id: Story owner ID. 
		:param story_id: Story ID.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getStats", params)
        model = stories.GetStatsResponse
        return model(**response).response

    async def get_video_upload_server(
        self,
		add_to_news: Optional[bool] = None,
		user_ids: Optional[List[int]] = None,
		reply_to_story: Optional[str] = None,
		link_text: Optional[str] = None,
		link_url: Optional[str] = None,
		group_id: Optional[int] = None,
		clickable_stickers: Optional[str] = None,
		**kwargs
    ) -> stories.GetVideoUploadServerResponseModel:
        """Allows to receive URL for uploading story with video.
		:param add_to_news: 1 — to add the story to friend's feed.
		:param user_ids: List of users IDs who can see the story.
		:param reply_to_story: ID of the story to reply with the current.
		:param link_text: Link text (for community's stories only).
		:param link_url: Link URL. Internal links on https://vk.com only.
		:param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
		:param clickable_stickers: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getVideoUploadServer", params)
        model = stories.GetVideoUploadServerResponse
        return model(**response).response

    async def get_viewers(
        self,
		owner_id: int,
		story_id: int,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		extended: Optional[bool] = None,
		**kwargs
    ) -> stories.GetViewersResponseModel:
        """Returns a list of story viewers.
		:param owner_id: Story owner ID.
		:param story_id: Story ID.
		:param count: Maximum number of results.
		:param offset: Offset needed to return a specific subset of results.
		:param extended: '1' — to return detailed information about photos
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getViewers", params)
        model = stories.GetViewersResponse
        return model(**response).response

    async def hide_all_replies(
        self, owner_id: int, group_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Hides all replies in the last 24 hours from the user to current user's stories.
		:param owner_id: ID of the user whose replies should be hidden.
		:param group_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.hideAllReplies", params)
        model = base.OkResponse
        return model(**response).response

    async def hide_reply(
        self, owner_id: int, story_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Hides the reply to the current user's story.
		:param owner_id: ID of the user whose replies should be hidden.
		:param story_id: Story ID.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.hideReply", params)
        model = base.OkResponse
        return model(**response).response

    async def save(
        self, upload_results: List[str], **kwargs
    ) -> stories.SaveResponseModel:
        """stories.save method
		:param upload_results: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.save", params)
        model = stories.SaveResponse
        return model(**response).response

    async def search(
        self,
		q: Optional[str] = None,
		place_id: Optional[int] = None,
		latitude: Optional[number] = None,
		longitude: Optional[number] = None,
		radius: Optional[int] = None,
		mentioned_id: Optional[int] = None,
		count: Optional[int] = None,
		extended: Optional[bool] = None,
		fields: Optional[List[str]] = None,
		**kwargs
    ) -> stories.SearchResponseModel:
        """stories.search method
		:param q: 
		:param place_id: 
		:param latitude: 
		:param longitude: 
		:param radius: 
		:param mentioned_id: 
		:param count: 
		:param extended: 
		:param fields: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.search", params)
        model = stories.SearchResponse
        return model(**response).response

    async def send_interaction(
        self,
		access_key: str,
		message: Optional[str] = None,
		is_broadcast: Optional[bool] = None,
		is_anonymous: Optional[bool] = None,
		unseen_marker: Optional[bool] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """stories.sendInteraction method
		:param access_key: 
		:param message: 
		:param is_broadcast: 
		:param is_anonymous: 
		:param unseen_marker: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.sendInteraction", params)
        model = base.OkResponse
        return model(**response).response

    async def unban_owner(
        self, owners_ids: List[int], **kwargs
    ) -> base.OkResponseModel:
        """Allows to show stories from hidden sources in current user's feed.
		:param owners_ids: List of hidden sources to show stories from.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("stories.unbanOwner", params)
        model = base.OkResponse
        return model(**response).response