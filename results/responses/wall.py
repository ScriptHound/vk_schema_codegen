


class CreateCommentResponse(BaseResponse):
	response = None


class EditResponse(BaseResponse):
	response = None


class GetByIdExtendedResponse(BaseResponse):
	response = None


class GetByIdLegacyResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetCommentExtendedResponse(BaseResponse):
	response = None


class GetCommentResponse(BaseResponse):
	response = None


class GetCommentsExtendedResponse(BaseResponse):
	response = None


class GetCommentsResponse(BaseResponse):
	response = None


class GetRepostsResponse(BaseResponse):
	response = None


class GetExtendedResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class PostAdsStealthResponse(BaseResponse):
	response = None


class PostResponse(BaseResponse):
	response = None


class RepostResponse(BaseResponse):
	response = None


class SearchExtendedResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class CreateCommentResponse(BaseResponse):
	comment_id = None


class EditResponse(BaseResponse):
	post_id = None


class GetByIdExtendedResponse(BaseResponse):
	items = None
	profiles = None
	groups = None


GetByIdLegacyResponseModel = array


class GetByIdResponse(BaseResponse):
	items = None


class GetCommentExtendedResponse(BaseResponse):
	items = None
	profiles = None
	groups = None


class GetCommentResponse(BaseResponse):
	items = None


class GetCommentsExtendedResponse(BaseResponse):
	count = None
	items = None
	show_reply_button = None
	can_post = None
	groups_can_post = None
	current_level_count = None
	profiles = None
	groups = None


class GetCommentsResponse(BaseResponse):
	count = None
	items = None
	can_post = None
	groups_can_post = None
	current_level_count = None


class GetRepostsResponse(BaseResponse):
	items = None
	profiles = None
	groups = None


class GetExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class GetResponse(BaseResponse):
	count = None
	items = None


class PostAdsStealthResponse(BaseResponse):
	post_id = None


class PostResponse(BaseResponse):
	post_id = None


class RepostResponse(BaseResponse):
	success = None
	post_id = None
	reposts_count = None
	wall_repost_count = None
	mail_repost_count = None
	likes_count = None


class SearchExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class SearchResponse(BaseResponse):
	count = None
	items = None