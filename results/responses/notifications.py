from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class MarkAsViewedResponse(BaseResponse):
	response: Optional["MarkAsViewedResponseModel"] = None


class SendMessageResponse(BaseResponse):
	response: Optional["SendMessageResponseModel"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	last_viewed: Optional["integer"] = None
	photos: Optional["array"] = None
	videos: Optional["array"] = None
	apps: Optional["array"] = None
	next_from: Optional["string"] = None
	ttl: Optional["integer"] = None


MarkAsViewedResponseModel = Optional[Baseboolint]


SendMessageResponseModel = List[NotificationsSendMessageItem]

GetResponse.update_forward_refs()
MarkAsViewedResponse.update_forward_refs()
SendMessageResponse.update_forward_refs()
