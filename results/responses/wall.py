from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class EditResponse(BaseResponse):
	response: Optional["EditResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
	response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdLegacyResponse(BaseResponse):
	response: Optional["GetByIdLegacyResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetCommentExtendedResponse(BaseResponse):
	response: Optional["GetCommentExtendedResponseModel"] = None


class GetCommentResponse(BaseResponse):
	response: Optional["GetCommentResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
	response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetRepostsResponse(BaseResponse):
	response: Optional["GetRepostsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class PostAdsStealthResponse(BaseResponse):
	response: Optional["PostAdsStealthResponseModel"] = None


class PostResponse(BaseResponse):
	response: Optional["PostResponseModel"] = None


class RepostResponse(BaseResponse):
	response: Optional["RepostResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
	response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class CreateCommentResponseModel(BaseResponse):
	comment_id: Optional["integer"] = None


class EditResponseModel(BaseResponse):
	post_id: Optional["integer"] = None


class GetByIdExtendedResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


GetByIdLegacyResponseModel = List[WallWallpostFull]


class GetByIdResponseModel(BaseResponse):
	items: Optional["array"] = None


class GetCommentExtendedResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetCommentResponseModel(BaseResponse):
	items: Optional["array"] = None


class GetCommentsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	show_reply_button: Optional["boolean"] = None
	can_post: Optional["boolean"] = None
	groups_can_post: Optional["boolean"] = None
	current_level_count: Optional["integer"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	can_post: Optional["boolean"] = None
	groups_can_post: Optional["boolean"] = None
	current_level_count: Optional["integer"] = None


class GetRepostsResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class PostAdsStealthResponseModel(BaseResponse):
	post_id: Optional["integer"] = None


class PostResponseModel(BaseResponse):
	post_id: Optional["integer"] = None


class RepostResponseModel(BaseResponse):
	success: Optional["integer"] = None
	post_id: Optional["integer"] = None
	reposts_count: Optional["integer"] = None
	wall_repost_count: Optional["integer"] = None
	mail_repost_count: Optional["integer"] = None
	likes_count: Optional["integer"] = None


class SearchExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class SearchResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None

CreateCommentResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdLegacyResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentExtendedResponse.update_forward_refs()
GetCommentResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetRepostsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
PostAdsStealthResponse.update_forward_refs()
PostResponse.update_forward_refs()
RepostResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()
