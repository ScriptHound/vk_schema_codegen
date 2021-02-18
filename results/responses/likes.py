from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class AddResponse(BaseResponse):
	response: Optional["AddResponseModel"] = None


class DeleteResponse(BaseResponse):
	response: Optional["DeleteResponseModel"] = None


class GetListExtendedResponse(BaseResponse):
	response: Optional["GetListExtendedResponseModel"] = None


class GetListResponse(BaseResponse):
	response: Optional["GetListResponseModel"] = None


class IsLikedResponse(BaseResponse):
	response: Optional["IsLikedResponseModel"] = None


class AddResponseModel(BaseResponse):
	likes: Optional["integer"] = None


class DeleteResponseModel(BaseResponse):
	likes: Optional["integer"] = None


class GetListExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetListResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class IsLikedResponseModel(BaseResponse):
	liked: Optional["baseboolint"] = None
	copied: Optional["baseboolint"] = None

AddResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
GetListExtendedResponse.update_forward_refs()
GetListResponse.update_forward_refs()
IsLikedResponse.update_forward_refs()