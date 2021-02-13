from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddAddressResponse(BaseResponse):
	response: Optional["AddAddressResponseModel"] = None


class AddCallbackServerResponse(BaseResponse):
	response: Optional["AddCallbackServerResponseModel"] = None


class AddLinkResponse(BaseResponse):
	response: Optional["AddLinkResponseModel"] = None


class CreateResponse(BaseResponse):
	response: Optional["CreateResponseModel"] = None


class EditAddressResponse(BaseResponse):
	response: Optional["EditAddressResponseModel"] = None


class GetAddressesResponse(BaseResponse):
	response: Optional["GetAddressesResponseModel"] = None


class GetBannedResponse(BaseResponse):
	response: Optional["GetBannedResponseModel"] = None


class GetByIdLegacyResponse(BaseResponse):
	response: Optional["GetByIdLegacyResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
	response: Optional["GetCallbackConfirmationCodeResponseModel"] = None


class GetCallbackServersResponse(BaseResponse):
	response: Optional["GetCallbackServersResponseModel"] = None


class GetCallbackSettingsResponse(BaseResponse):
	response: Optional["GetCallbackSettingsResponseModel"] = None


class GetCatalogInfoExtendedResponse(BaseResponse):
	response: Optional["GetCatalogInfoExtendedResponseModel"] = None


class GetCatalogInfoResponse(BaseResponse):
	response: Optional["GetCatalogInfoResponseModel"] = None


class GetCatalogResponse(BaseResponse):
	response: Optional["GetCatalogResponseModel"] = None


class GetInvitedUsersResponse(BaseResponse):
	response: Optional["GetInvitedUsersResponseModel"] = None


class GetInvitesExtendedResponse(BaseResponse):
	response: Optional["GetInvitesExtendedResponseModel"] = None


class GetInvitesResponse(BaseResponse):
	response: Optional["GetInvitesResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
	response: Optional["GetLongPollServerResponseModel"] = None


class GetLongPollSettingsResponse(BaseResponse):
	response: Optional["GetLongPollSettingsResponseModel"] = None


class GetMembersFieldsResponse(BaseResponse):
	response: Optional["GetMembersFieldsResponseModel"] = None


class GetMembersFilterResponse(BaseResponse):
	response: Optional["GetMembersFilterResponseModel"] = None


class GetMembersResponse(BaseResponse):
	response: Optional["GetMembersResponseModel"] = None


class GetRequestsFieldsResponse(BaseResponse):
	response: Optional["GetRequestsFieldsResponseModel"] = None


class GetRequestsResponse(BaseResponse):
	response: Optional["GetRequestsResponseModel"] = None


class GetSettingsResponse(BaseResponse):
	response: Optional["GetSettingsResponseModel"] = None


class GetTagListResponse(BaseResponse):
	response: Optional["GetTagListResponseModel"] = None


class GetTokenPermissionsResponse(BaseResponse):
	response: Optional["GetTokenPermissionsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class IsMemberExtendedResponse(BaseResponse):
	response: Optional["IsMemberExtendedResponseModel"] = None


class IsMemberResponse(BaseResponse):
	response: Optional["IsMemberResponseModel"] = None


class IsMemberUserIdsExtendedResponse(BaseResponse):
	response: Optional["IsMemberUserIdsExtendedResponseModel"] = None


class IsMemberUserIdsResponse(BaseResponse):
	response: Optional["IsMemberUserIdsResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


AddAddressResponseModelModel = None


class AddCallbackServerResponseModel(BaseResponse):
	server_id: Optional[int] = None


AddLinkResponseModelModel = None


CreateResponseModelModel = None


EditAddressResponseModelModel = None


class GetAddressesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetBannedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetByIdLegacyResponseModelModel = array


class GetByIdResponseModel(BaseResponse):
	groups: Optional["Array"] = None
	profiles: Optional["Array"] = None


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
	code: Optional[str] = None


class GetCallbackServersResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetCallbackSettingsResponseModelModel = None


class GetCatalogInfoExtendedResponseModel(BaseResponse):
	enabled: Optional[int] = None
	categories: Optional["Array"] = None


class GetCatalogInfoResponseModel(BaseResponse):
	enabled: Optional[int] = None
	categories: Optional["Array"] = None


class GetCatalogResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetInvitedUsersResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetInvitesExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None
	profiles: Optional["Array"] = None
	groups: Optional["Array"] = None


class GetInvitesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetLongPollServerResponseModelModel = None


GetLongPollSettingsResponseModelModel = None


class GetMembersFieldsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetMembersFilterResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetMembersResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetRequestsFieldsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetRequestsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetSettingsResponseModel(BaseResponse):
	access = None
	address = None
	audio = None
	articles = None
	recognize_photo = None
	city_id = None
	contacts = None
	links = None
	sections_list = None
	main_section = None
	secondary_section = None
	age_limits = None
	country_id = None
	description = None
	docs = None
	events = None
	obscene_filter = None
	obscene_stopwords = None
	obscene_words = None
	event_group_id = None
	photos = None
	public_category = None
	public_category_list = None
	public_date = None
	public_date_label = None
	public_subcategory = None
	rss = None
	start_date = None
	finish_date = None
	subject = None
	subject_list = None
	suggested_privacy = None
	title = None
	topics = None
	twitter = None
	video = None
	wall = None
	website = None
	phone = None
	email = None
	wiki = None


GetTagListResponseModelModel = array


class GetTokenPermissionsResponseModel(BaseResponse):
	mask: Optional[int] = None
	permissions: Optional["Array"] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class IsMemberExtendedResponseModel(BaseResponse):
	member = None
	invitation = None
	can_invite = None
	can_recall = None
	request = None


IsMemberResponseModelModel = None


IsMemberUserIdsExtendedResponseModelModel = array


IsMemberUserIdsResponseModelModel = array


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None

AddAddressResponse.update_forward_refs()
AddCallbackServerResponse.update_forward_refs()
AddLinkResponse.update_forward_refs()
CreateResponse.update_forward_refs()
EditAddressResponse.update_forward_refs()
GetAddressesResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetByIdLegacyResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCallbackConfirmationCodeResponse.update_forward_refs()
GetCallbackServersResponse.update_forward_refs()
GetCallbackSettingsResponse.update_forward_refs()
GetCatalogInfoExtendedResponse.update_forward_refs()
GetCatalogInfoResponse.update_forward_refs()
GetCatalogResponse.update_forward_refs()
GetInvitedUsersResponse.update_forward_refs()
GetInvitesExtendedResponse.update_forward_refs()
GetInvitesResponse.update_forward_refs()
GetLongPollServerResponse.update_forward_refs()
GetLongPollSettingsResponse.update_forward_refs()
GetMembersFieldsResponse.update_forward_refs()
GetMembersFilterResponse.update_forward_refs()
GetMembersResponse.update_forward_refs()
GetRequestsFieldsResponse.update_forward_refs()
GetRequestsResponse.update_forward_refs()
GetSettingsResponse.update_forward_refs()
GetTagListResponse.update_forward_refs()
GetTokenPermissionsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
IsMemberExtendedResponse.update_forward_refs()
IsMemberResponse.update_forward_refs()
IsMemberUserIdsExtendedResponse.update_forward_refs()
IsMemberUserIdsResponse.update_forward_refs()
SearchResponse.update_forward_refs()
