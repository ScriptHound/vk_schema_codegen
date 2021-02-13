from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetSubscriptionResponse(BaseResponse):
	response: Optional["GetSubscriptionResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
	response: Optional["GetSubscriptionsResponseModel"] = None


GetSubscriptionResponseModelModel = None


class GetSubscriptionsResponseModel(BaseResponse):
	subscriptions: Optional["Array"] = None
	count: Optional[int] = None
	profiles: Optional["Array"] = None
	groups: Optional["Array"] = None

GetSubscriptionResponse.update_forward_refs()
GetSubscriptionsResponse.update_forward_refs()
