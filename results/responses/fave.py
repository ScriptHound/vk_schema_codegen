from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddTagResponse(BaseResponse):
	response: Optional["AddTagResponseModel"] = None


class GetPagesResponse(BaseResponse):
	response: Optional["GetPagesResponseModel"] = None


class GetTagsResponse(BaseResponse):
	response: Optional["GetTagsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


AddTagResponseModel = Optional[Favetag]


class GetPagesResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetTagsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None

AddTagResponse.update_forward_refs()
GetPagesResponse.update_forward_refs()
GetTagsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
