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


AddAddressResponseModel = Optional[Groupsaddress]


class AddCallbackServerResponseModel(BaseResponse):
	server_id: Optional["integer"] = None


AddLinkResponseModel = Optional[Groupsgrouplink]


CreateResponseModel = Optional[Groupsgroup]


EditAddressResponseModel = Optional[Groupsaddress]


class GetAddressesResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetBannedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetByIdLegacyResponseModel = List[GroupsGroupFull]


class GetByIdResponseModel(BaseResponse):
	groups: Optional["array"] = None
	profiles: Optional["array"] = None


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
	code: Optional["string"] = None


class GetCallbackServersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetCallbackSettingsResponseModel = Optional[Groupscallbacksettings]


class GetCatalogInfoExtendedResponseModel(BaseResponse):
	enabled: Optional["integer"] = None
	categories: Optional["array"] = None


class GetCatalogInfoResponseModel(BaseResponse):
	enabled: Optional["integer"] = None
	categories: Optional["array"] = None


class GetCatalogResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetInvitedUsersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetInvitesExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetInvitesResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetLongPollServerResponseModel = Optional[Groupslongpollserver]


GetLongPollSettingsResponseModel = Optional[Groupslongpollsettings]


class GetMembersFieldsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetMembersFilterResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetMembersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetRequestsFieldsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetRequestsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetSettingsResponseModel(BaseResponse):
	access: Optional["groupsgroupaccess"] = None
	address: Optional["string"] = None
	audio: Optional["groupsgroupaudio"] = None
	articles: Optional["integer"] = None
	recognize_photo: Optional["integer"] = None
	city_id: Optional["integer"] = None
	contacts: Optional["baseboolint"] = None
	links: Optional["baseboolint"] = None
	sections_list: Optional["array"] = None
	main_section: Optional["groupsgroupfullmainsection"] = None
	secondary_section: Optional["integer"] = None
	age_limits: Optional["groupsgroupagelimits"] = None
	country_id: Optional["integer"] = None
	description: Optional["string"] = None
	docs: Optional["groupsgroupdocs"] = None
	events: Optional["baseboolint"] = None
	obscene_filter: Optional["baseboolint"] = None
	obscene_stopwords: Optional["baseboolint"] = None
	obscene_words: Optional["array"] = None
	event_group_id: Optional["integer"] = None
	photos: Optional["groupsgroupphotos"] = None
	public_category: Optional["integer"] = None
	public_category_list: Optional["array"] = None
	public_date: Optional["string"] = None
	public_date_label: Optional["string"] = None
	public_subcategory: Optional["integer"] = None
	rss: Optional["string"] = None
	start_date: Optional["integer"] = None
	finish_date: Optional["integer"] = None
	subject: Optional["integer"] = None
	subject_list: Optional["array"] = None
	suggested_privacy: Optional["groupsgroupsuggestedprivacy"] = None
	title: Optional["string"] = None
	topics: Optional["groupsgrouptopics"] = None
	twitter: Optional["groupssettingstwitter"] = None
	video: Optional["groupsgroupvideo"] = None
	wall: Optional["groupsgroupwall"] = None
	website: Optional["string"] = None
	phone: Optional["string"] = None
	email: Optional["string"] = None
	wiki: Optional["groupsgroupwiki"] = None


GetTagListResponseModel = List[GroupsGroupTag]


class GetTokenPermissionsResponseModel(BaseResponse):
	mask: Optional["integer"] = None
	permissions: Optional["array"] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class IsMemberExtendedResponseModel(BaseResponse):
	member: Optional["baseboolint"] = None
	invitation: Optional["baseboolint"] = None
	can_invite: Optional["baseboolint"] = None
	can_recall: Optional["baseboolint"] = None
	request: Optional["baseboolint"] = None


IsMemberResponseModel = Optional[Baseboolint]


IsMemberUserIdsExtendedResponseModel = List[GroupsMemberStatusFull]


IsMemberUserIdsResponseModel = List[GroupsMemberStatus]


class SearchResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None

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