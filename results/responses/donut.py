from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetSubscriptionResponse(BaseResponse):
	response: Optional["GetSubscriptionResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
	response: Optional["GetSubscriptionsResponseModel"] = None


GetSubscriptionResponseModel = Optional[Donutdonatorsubscriptioninfo]


class GetSubscriptionsResponseModel(BaseResponse):
	subscriptions: Optional["array"] = None
	count: Optional["integer"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None

GetSubscriptionResponse.update_forward_refs()
GetSubscriptionsResponse.update_forward_refs()
