from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddTopicResponse(BaseResponse):
	response: Optional["AddTopicResponseModel"] = None


class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
	response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetTopicsExtendedResponse(BaseResponse):
	response: Optional["GetTopicsExtendedResponseModel"] = None


class GetTopicsResponse(BaseResponse):
	response: Optional["GetTopicsResponseModel"] = None


AddTopicResponseModel = int


CreateCommentResponseModel = int


class GetCommentsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	poll: Optional["boardtopicpoll"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	poll: Optional["boardtopicpoll"] = None


class GetTopicsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	default_order: Optional["boarddefaultorder"] = None
	can_add_topics: Optional["baseboolint"] = None
	profiles: Optional["array"] = None


class GetTopicsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	default_order: Optional["boarddefaultorder"] = None
	can_add_topics: Optional["baseboolint"] = None

AddTopicResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetTopicsExtendedResponse.update_forward_refs()
GetTopicsResponse.update_forward_refs()
