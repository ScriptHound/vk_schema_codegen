from enum import N, o, n, e
from typing import Any, List, Optional, Union
from pydantic import BaseModel

class AccountAccountCounters(BaseModel):
	"""VK Object AccountAccountCounters

	app_requests - New app requests number
	events - New events number
	faves - New faves number
	friends - New friends requests number
	friends_suggestions - New friends suggestions number
	friends_recommendations - New friends recommendations number
	gifts - New gifts number
	groups - New groups number
	menu_discover_badge - 
	menu_clips_badge - 
	messages - New messages number
	memories - New memories number
	notes - New notes number
	notifications - New notifications number
	photos - New photo tags number
	sdk - New sdk number
	"""
	app_requests: Optional["integer"] = None
	events: Optional["integer"] = None
	faves: Optional["integer"] = None
	friends: Optional["integer"] = None
	friends_suggestions: Optional["integer"] = None
	friends_recommendations: Optional["integer"] = None
	gifts: Optional["integer"] = None
	groups: Optional["integer"] = None
	menu_discover_badge: Optional["integer"] = None
	menu_clips_badge: Optional["integer"] = None
	messages: Optional["integer"] = None
	memories: Optional["integer"] = None
	notes: Optional["integer"] = None
	notifications: Optional["integer"] = None
	photos: Optional["integer"] = None
	sdk: Optional["integer"] = None


class AccountInfo(BaseModel):
	"""VK Object AccountInfo

	wishlists_ae_promo_banner_show - 
	2fa_required - Two factor authentication is enabled
	country - Country code
	https_required - Information whether HTTPS-only is enabled
	intro - Information whether user has been processed intro
	show_vk_apps_intro - 
	mini_apps_ads_slot_id - Ads slot id for MyTarget
	qr_promotion - 
	link_redirects - 
	lang - Language ID
	no_wall_replies - Information whether wall comments should be hidden
	own_posts_default - Information whether only owners posts should be shown
	subscriptions - 
	"""
	wishlists_ae_promo_banner_show: Optional["baseboolint"] = None
	_2fa_required: Optional["baseboolint"] = None
	country: Optional["string"] = None
	https_required: Optional["baseboolint"] = None
	intro: Optional["baseboolint"] = None
	show_vk_apps_intro: Optional["boolean"] = None
	mini_apps_ads_slot_id: Optional["integer"] = None
	qr_promotion: Optional["integer"] = None
	link_redirects: Optional["object"] = None
	lang: Optional["integer"] = None
	no_wall_replies: Optional["baseboolint"] = None
	own_posts_default: Optional["baseboolint"] = None
	subscriptions: Optional["integer"] = None


class AccountNameRequest(BaseModel):
	"""VK Object AccountNameRequest

	first_name - First name in request
	id - Request ID needed to cancel the request
	last_name - Last name in request
	status - 
	lang - Text to display to user
	link_href - href for link in lang field
	link_label - label to display for link in lang field
	"""
	first_name: Optional["string"] = None
	id: Optional["integer"] = None
	last_name: Optional["string"] = None
	status: Optional["accountnamerequeststatus"] = None
	lang: Optional["string"] = None
	link_href: Optional["string"] = None
	link_label: Optional["string"] = None


class AccountNameRequestStatus(enum.Enum):
	"""VK Object AccountNameRequestStatus

	"""
	SUCCESS = "success"
	PROCESSING = "processing"
	DECLINED = "declined"
	WAS_ACCEPTED = "was_accepted"
	WAS_DECLINED = "was_declined"
	DECLINED_WITH_LINK = "declined_with_link"
	RESPONSE = "response"
	RESPONSE_WITH_LINK = "response_with_link"


class AccountOffer(BaseModel):
	"""VK Object AccountOffer

	description - Offer description
	id - Offer ID
	img - URL of the preview image
	instruction - Instruction how to process the offer
	instruction_html - Instruction how to process the offer (HTML format)
	price - Offer price
	short_description - Offer short description
	tag - Offer tag
	title - Offer title
	currency_amount - Currency amount
	link_id - Link id
	link_type - Link type
	"""
	description: Optional["string"] = None
	id: Optional["integer"] = None
	img: Optional["string"] = None
	instruction: Optional["string"] = None
	instruction_html: Optional["string"] = None
	price: Optional["integer"] = None
	short_description: Optional["string"] = None
	tag: Optional["string"] = None
	title: Optional["string"] = None
	currency_amount: Optional["number"] = None
	link_id: Optional["integer"] = None
	link_type: Optional["string"] = None


class AccountPushConversations(BaseModel):
	"""VK Object AccountPushConversations

	count - Items count
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["accountpushconversationsitem"] = None


class AccountPushConversationsItem(BaseModel):
	"""VK Object AccountPushConversationsItem

	disabled_until - Time until that notifications are disabled in seconds
	peer_id - Peer ID
	sound - Information whether the sound are enabled
	"""
	disabled_until: Optional["integer"] = None
	peer_id: Optional["integer"] = None
	sound: Optional["baseboolint"] = None


class AccountPushParams(BaseModel):
	"""VK Object AccountPushParams

	"""
	msg: Optional["accountpushparamsmode"] = None
	chat: Optional["accountpushparamsmode"] = None
	like: Optional["accountpushparamssettings"] = None
	repost: Optional["accountpushparamssettings"] = None
	comment: Optional["accountpushparamssettings"] = None
	mention: Optional["accountpushparamssettings"] = None
	reply: Optional["accountpushparamsonoff"] = None
	new_post: Optional["accountpushparamsonoff"] = None
	wall_post: Optional["accountpushparamsonoff"] = None
	wall_publish: Optional["accountpushparamsonoff"] = None
	friend: Optional["accountpushparamsonoff"] = None
	friend_found: Optional["accountpushparamsonoff"] = None
	friend_accepted: Optional["accountpushparamsonoff"] = None
	group_invite: Optional["accountpushparamsonoff"] = None
	group_accepted: Optional["accountpushparamsonoff"] = None
	birthday: Optional["accountpushparamsonoff"] = None
	event_soon: Optional["accountpushparamsonoff"] = None
	app_request: Optional["accountpushparamsonoff"] = None
	sdk_open: Optional["accountpushparamsonoff"] = None


class AccountPushParamsMode(enum.Enum):
	"""VK Object AccountPushParamsMode

	"""
	ON = "on"
	OFF = "off"
	NO_SOUND = "no_sound"
	NO_TEXT = "no_text"


class AccountPushParamsOnoff(enum.Enum):
	"""VK Object AccountPushParamsOnoff

	"""
	ON = "on"
	OFF = "off"


class AccountPushParamsSettings(enum.Enum):
	"""VK Object AccountPushParamsSettings

	"""
	ON = "on"
	OFF = "off"
	FR_OF_FR = "fr_of_fr"


class AccountPushSettings(BaseModel):
	"""VK Object AccountPushSettings

	disabled - Information whether notifications are disabled
	disabled_until - Time until that notifications are disabled in Unixtime
	settings - 
	conversations - 
	"""
	disabled: Optional["baseboolint"] = None
	disabled_until: Optional["integer"] = None
	settings: Optional["accountpushparams"] = None
	conversations: Optional["accountpushconversations"] = None


class AccountUserSettings(UsersUserMin,
	UsersUserSettingsXtr):
	"""VK Object AccountUserSettings

	photo_200 - URL of square photo of the user with 200 pixels in width
	is_service_account - flag about service account
	"""
	photo_200 = None
	is_service_account = None


class AccountUserSettingsInterest(BaseModel):
	"""VK Object AccountUserSettingsInterest

	"""
	title: Optional["string"] = None
	value: Optional["string"] = None


class AccountUserSettingsInterests(BaseModel):
	"""VK Object AccountUserSettingsInterests

	"""
	activities: Optional["accountusersettingsinterest"] = None
	interests: Optional["accountusersettingsinterest"] = None
	music: Optional["accountusersettingsinterest"] = None
	tv: Optional["accountusersettingsinterest"] = None
	movies: Optional["accountusersettingsinterest"] = None
	books: Optional["accountusersettingsinterest"] = None
	games: Optional["accountusersettingsinterest"] = None
	quotes: Optional["accountusersettingsinterest"] = None
	about: Optional["accountusersettingsinterest"] = None


class AddressesFields(enum.Enum):
	"""VK Object AddressesFields

	"""
	ID = "id"
	TITLE = "title"
	ADDRESS = "address"
	ADDITIONAL_ADDRESS = "additional_address"
	COUNTRY_ID = "country_id"
	CITY_ID = "city_id"
	METRO_STATION_ID = "metro_station_id"
	LATITUDE = "latitude"
	LONGITUDE = "longitude"
	DISTANCE = "distance"
	WORK_INFO_STATUS = "work_info_status"
	TIMETABLE = "timetable"
	PHONE = "phone"
	TIME_OFFSET = "time_offset"


class AdsAccessRole(enum.Enum):
	"""VK Object AdsAccessRole

	"""
	ADMIN = "admin"
	MANAGER = "manager"
	REPORTS = "reports"


class AdsAccessRolePublic(enum.Enum):
	"""VK Object AdsAccessRolePublic

	"""
	MANAGER = "manager"
	REPORTS = "reports"


class AdsAccesses(BaseModel):
	"""VK Object AdsAccesses

	client_id - Client ID
	role - 
	"""
	client_id: Optional["string"] = None
	role: Optional["adsaccessrole"] = None


class AdsAccount(BaseModel):
	"""VK Object AdsAccount

	access_role - 
	account_id - Account ID
	account_status - Information whether account is active
	account_type - 
	account_name - Account name
	can_view_budget - Can user view account budget
	"""
	access_role: Optional["adsaccessrole"] = None
	account_id: Optional["integer"] = None
	account_status: Optional["baseboolint"] = None
	account_type: Optional["adsaccounttype"] = None
	account_name: Optional["string"] = None
	can_view_budget: Optional["boolean"] = None


class AdsAccountType(enum.Enum):
	"""VK Object AdsAccountType

	"""
	GENERAL = "general"
	AGENCY = "agency"


class AdsAd(BaseModel):
	"""VK Object AdsAd

	ad_format - Ad format
	ad_platform - Ad platform
	all_limit - Total limit
	approved - 
	campaign_id - Campaign ID
	category1_id - Category ID
	category2_id - Additional category ID
	cost_type - 
	cpc - Cost of a click, kopecks
	cpm - Cost of 1000 impressions, kopecks
	cpa - Cost of an action, kopecks
	ocpm - Cost of 1000 impressions optimized, kopecks
	autobidding_max_cost - Max cost of target actions for autobidding, kopecks
	disclaimer_medical - Information whether disclaimer is enabled
	disclaimer_specialist - Information whether disclaimer is enabled
	disclaimer_supplements - Information whether disclaimer is enabled
	id - Ad ID
	impressions_limit - Impressions limit
	impressions_limited - Information whether impressions are limited
	name - Ad title
	status - 
	video - Information whether the ad is a video
	"""
	ad_format: Optional["integer"] = None
	ad_platform: Optional[Union[int, str]] = None
	all_limit: Optional["integer"] = None
	approved: Optional["adsadapproved"] = None
	campaign_id: Optional["integer"] = None
	category1_id: Optional["integer"] = None
	category2_id: Optional["integer"] = None
	cost_type: Optional["adsadcosttype"] = None
	cpc: Optional["integer"] = None
	cpm: Optional["integer"] = None
	cpa: Optional["integer"] = None
	ocpm: Optional["integer"] = None
	autobidding_max_cost: Optional["integer"] = None
	disclaimer_medical: Optional["baseboolint"] = None
	disclaimer_specialist: Optional["baseboolint"] = None
	disclaimer_supplements: Optional["baseboolint"] = None
	id: Optional["integer"] = None
	impressions_limit: Optional["integer"] = None
	impressions_limited: Optional["baseboolint"] = None
	name: Optional["string"] = None
	status: Optional["adsadstatus"] = None
	video: Optional["baseboolint"] = None


class AdsAdApproved(enum.IntEnum):
	"""VK Object AdsAdApproved

	"""
	not moderated = 0
	pending moderation = 1
	approved = 2
	rejected = 3


class AdsAdCostType(enum.IntEnum):
	"""VK Object AdsAdCostType

	"""
	per clicks = 0
	per impressions = 1
	per actions = 2
	per impressions optimized = 3


class AdsAdLayout(BaseModel):
	"""VK Object AdsAdLayout

	ad_format - Ad format
	campaign_id - Campaign ID
	cost_type - 
	description - Ad description
	id - Ad ID
	image_src - Image URL
	image_src_2x - URL of the preview image in double size
	link_domain - Domain of advertised object
	link_url - URL of advertised object
	preview_link - link to preview an ad as it is shown on the website
	title - Ad title
	video - Information whether the ad is a video
	"""
	ad_format: Optional["integer"] = None
	campaign_id: Optional["integer"] = None
	cost_type: Optional["adsadcosttype"] = None
	description: Optional["string"] = None
	id: Optional["string"] = None
	image_src: Optional["string"] = None
	image_src_2x: Optional["string"] = None
	link_domain: Optional["string"] = None
	link_url: Optional["string"] = None
	preview_link: Optional[Union[int, str]] = None
	title: Optional["string"] = None
	video: Optional["baseboolint"] = None


class AdsAdStatus(enum.IntEnum):
	"""VK Object AdsAdStatus

	"""
	stopped = 0
	started = 1
	deleted = 2


class AdsCampaign(BaseModel):
	"""VK Object AdsCampaign

	all_limit - Campaign's total limit, rubles
	day_limit - Campaign's day limit, rubles
	id - Campaign ID
	name - Campaign title
	start_time - Campaign start time, as Unixtime
	status - 
	stop_time - Campaign stop time, as Unixtime
	type - 
	"""
	all_limit: Optional["string"] = None
	day_limit: Optional["string"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None
	start_time: Optional["integer"] = None
	status: Optional["adscampaignstatus"] = None
	stop_time: Optional["integer"] = None
	type: Optional["adscampaigntype"] = None


class AdsCampaignStatus(enum.IntEnum):
	"""VK Object AdsCampaignStatus

	"""
	stopped = 0
	started = 1
	deleted = 2


class AdsCampaignType(enum.Enum):
	"""VK Object AdsCampaignType

	"""
	NORMAL = "normal"
	VK_APPS_MANAGED = "vk_apps_managed"
	MOBILE_APPS = "mobile_apps"
	PROMOTED_POSTS = "promoted_posts"


class AdsCategory(BaseModel):
	"""VK Object AdsCategory

	id - Category ID
	name - Category name
	subcategories - 
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	subcategories: Optional["baseobjectwithname"] = None


class AdsClient(BaseModel):
	"""VK Object AdsClient

	all_limit - Client's total limit, rubles
	day_limit - Client's day limit, rubles
	id - Client ID
	name - Client name
	"""
	all_limit: Optional["string"] = None
	day_limit: Optional["string"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None


class AdsCriteria(BaseModel):
	"""VK Object AdsCriteria

	age_from - Age from
	age_to - Age to
	apps - Apps IDs
	apps_not - Apps IDs to except
	birthday - Days to birthday
	cities - Cities IDs
	cities_not - Cities IDs to except
	country - Country ID
	districts - Districts IDs
	groups - Communities IDs
	interest_categories - Interests categories IDs
	interests - Interests
	paying - Information whether the user has proceeded VK payments before
	positions - Positions IDs
	religions - Religions IDs
	retargeting_groups - Retargeting groups IDs
	retargeting_groups_not - Retargeting groups IDs to except
	school_from - School graduation year from
	school_to - School graduation year to
	schools - Schools IDs
	sex - 
	stations - Stations IDs
	statuses - Relationship statuses
	streets - Streets IDs
	travellers - Travellers only
	uni_from - University graduation year from
	uni_to - University graduation year to
	user_browsers - Browsers
	user_devices - Devices
	user_os - Operating systems
	"""
	age_from: Optional["integer"] = None
	age_to: Optional["integer"] = None
	apps: Optional["string"] = None
	apps_not: Optional["string"] = None
	birthday: Optional["integer"] = None
	cities: Optional["string"] = None
	cities_not: Optional["string"] = None
	country: Optional["integer"] = None
	districts: Optional["string"] = None
	groups: Optional["string"] = None
	interest_categories: Optional["string"] = None
	interests: Optional["string"] = None
	paying: Optional["baseboolint"] = None
	positions: Optional["string"] = None
	religions: Optional["string"] = None
	retargeting_groups: Optional["string"] = None
	retargeting_groups_not: Optional["string"] = None
	school_from: Optional["integer"] = None
	school_to: Optional["integer"] = None
	schools: Optional["string"] = None
	sex: Optional["adscriteriasex"] = None
	stations: Optional["string"] = None
	statuses: Optional["string"] = None
	streets: Optional["string"] = None
	travellers: Optional["basepropertyexists"] = None
	uni_from: Optional["integer"] = None
	uni_to: Optional["integer"] = None
	user_browsers: Optional["string"] = None
	user_devices: Optional["string"] = None
	user_os: Optional["string"] = None


class AdsCriteriaSex(enum.IntEnum):
	"""VK Object AdsCriteriaSex

	"""
	any = 0
	male = 1
	female = 2


class AdsDemoStats(BaseModel):
	"""VK Object AdsDemoStats

	id - Object ID
	stats - 
	type - 
	"""
	id: Optional["integer"] = None
	stats: Optional["adsdemostatsformat"] = None
	type: Optional["adsobjecttype"] = None


class AdsDemostatsFormat(BaseModel):
	"""VK Object AdsDemostatsFormat

	age - 
	cities - 
	day - Day as YYYY-MM-DD
	month - Month as YYYY-MM
	overall - 1 if period=overall
	sex - 
	sex_age - 
	"""
	age: Optional["adsstatsage"] = None
	cities: Optional["adsstatscities"] = None
	day: Optional["string"] = None
	month: Optional["string"] = None
	overall: Optional["integer"] = None
	sex: Optional["adsstatssex"] = None
	sex_age: Optional["adsstatssexage"] = None


class AdsFloodStats(BaseModel):
	"""VK Object AdsFloodStats

	left - Requests left
	refresh - Time to refresh in seconds
	"""
	left: Optional["integer"] = None
	refresh: Optional["integer"] = None


class AdsLinkStatus(BaseModel):
	"""VK Object AdsLinkStatus

	description - Reject reason
	redirect_url - URL
	status - Link status
	"""
	description: Optional["string"] = None
	redirect_url: Optional["string"] = None
	status: Optional["string"] = None


class AdsLookalikeRequest(BaseModel):
	"""VK Object AdsLookalikeRequest

	id - Lookalike request ID
	create_time - Lookalike request create time, as Unixtime
	update_time - Lookalike request update time, as Unixtime
	scheduled_delete_time - Time by which lookalike request would be deleted, as Unixtime
	status - Lookalike request status
	source_type - Lookalike request source type
	source_retargeting_group_id - Retargeting group id, which was used as lookalike seed
	source_name - Lookalike request seed name (retargeting group name)
	audience_count - Lookalike request seed audience size
	save_audience_levels - 
	"""
	id: Optional["integer"] = None
	create_time: Optional["integer"] = None
	update_time: Optional["integer"] = None
	scheduled_delete_time: Optional["integer"] = None
	status: Optional["string"] = None
	source_type: Optional["string"] = None
	source_retargeting_group_id: Optional["integer"] = None
	source_name: Optional["string"] = None
	audience_count: Optional["integer"] = None
	save_audience_levels: Optional["adslookalikerequestsaveaudiencelevel"] = None


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
	"""VK Object AdsLookalikeRequestSaveAudienceLevel

	level - Save audience level id, which is used in save audience queries
	audience_count - Saved audience audience size for according level
	"""
	level: Optional["integer"] = None
	audience_count: Optional["integer"] = None


class AdsMusician(BaseModel):
	"""VK Object AdsMusician

	id - Targeting music artist ID
	name - Music artist name
	avatar - Music artist photo
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	avatar: Optional["string"] = None


class AdsObjectType(enum.Enum):
	"""VK Object AdsObjectType

	"""
	AD = "ad"
	CAMPAIGN = "campaign"
	CLIENT = "client"
	OFFICE = "office"


class AdsParagraphs(BaseModel):
	"""VK Object AdsParagraphs

	paragraph - Rules paragraph
	"""
	paragraph: Optional["string"] = None


class AdsPromotedPostReach(BaseModel):
	"""VK Object AdsPromotedPostReach

	hide - Hides amount
	id - Object ID from 'ids' parameter
	join_group - Community joins
	links - Link clicks
	reach_subscribers - Subscribers reach
	reach_total - Total reach
	report - Reports amount
	to_group - Community clicks
	unsubscribe - 'Unsubscribe' events amount
	video_views_100p - Video views for 100 percent
	video_views_25p - Video views for 25 percent
	video_views_3s - Video views for 3 seconds
	video_views_50p - Video views for 50 percent
	video_views_75p - Video views for 75 percent
	video_views_start - Video starts
	"""
	hide: Optional["integer"] = None
	id: Optional["integer"] = None
	join_group: Optional["integer"] = None
	links: Optional["integer"] = None
	reach_subscribers: Optional["integer"] = None
	reach_total: Optional["integer"] = None
	report: Optional["integer"] = None
	to_group: Optional["integer"] = None
	unsubscribe: Optional["integer"] = None
	video_views_100p: Optional["integer"] = None
	video_views_25p: Optional["integer"] = None
	video_views_3s: Optional["integer"] = None
	video_views_50p: Optional["integer"] = None
	video_views_75p: Optional["integer"] = None
	video_views_start: Optional["integer"] = None


class AdsRejectReason(BaseModel):
	"""VK Object AdsRejectReason

	comment - Comment text
	rules - 
	"""
	comment: Optional["string"] = None
	rules: Optional["adsrules"] = None


class AdsRules(BaseModel):
	"""VK Object AdsRules

	paragraphs - 
	title - Comment
	"""
	paragraphs: Optional["adsparagraphs"] = None
	title: Optional["string"] = None


class AdsStats(BaseModel):
	"""VK Object AdsStats

	id - Object ID
	stats - 
	type - 
	views_times - 
	"""
	id: Optional["integer"] = None
	stats: Optional["adsstatsformat"] = None
	type: Optional["adsobjecttype"] = None
	views_times: Optional["adsstatsviewstimes"] = None


class AdsStatsAge(BaseModel):
	"""VK Object AdsStatsAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Age interval
	"""
	clicks_rate: Optional["number"] = None
	impressions_rate: Optional["number"] = None
	value: Optional["string"] = None


class AdsStatsCities(BaseModel):
	"""VK Object AdsStatsCities

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	name - City name
	value - City ID
	"""
	clicks_rate: Optional["number"] = None
	impressions_rate: Optional["number"] = None
	name: Optional["string"] = None
	value: Optional["integer"] = None


class AdsStatsFormat(BaseModel):
	"""VK Object AdsStatsFormat

	clicks - Clicks number
	day - Day as YYYY-MM-DD
	impressions - Impressions number
	join_rate - Events number
	month - Month as YYYY-MM
	overall - 1 if period=overall
	reach - Reach 
	spent - Spent funds
	video_clicks_site - Clickthoughs to the advertised site
	video_views - Video views number
	video_views_full - Video views (full video)
	video_views_half - Video views (half of video)
	"""
	clicks: Optional["integer"] = None
	day: Optional["string"] = None
	impressions: Optional["integer"] = None
	join_rate: Optional["integer"] = None
	month: Optional["string"] = None
	overall: Optional["integer"] = None
	reach: Optional["integer"] = None
	spent: Optional["integer"] = None
	video_clicks_site: Optional["integer"] = None
	video_views: Optional["integer"] = None
	video_views_full: Optional["integer"] = None
	video_views_half: Optional["integer"] = None


class AdsStatsSex(BaseModel):
	"""VK Object AdsStatsSex

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - 
	"""
	clicks_rate: Optional["number"] = None
	impressions_rate: Optional["number"] = None
	value: Optional["adsstatssexvalue"] = None


class AdsStatsSexAge(BaseModel):
	"""VK Object AdsStatsSexAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Sex and age interval
	"""
	clicks_rate: Optional["number"] = None
	impressions_rate: Optional["number"] = None
	value: Optional["string"] = None


class AdsStatsSexValue(enum.Enum):
	"""VK Object AdsStatsSexValue

	"""
	F = "f"
	M = "m"


class AdsStatsViewsTimes(BaseModel):
	"""VK Object AdsStatsViewsTimes

	"""
	views_ads_times_1: Optional["integer"] = None
	views_ads_times_2: Optional["integer"] = None
	views_ads_times_3: Optional["integer"] = None
	views_ads_times_4: Optional["integer"] = None
	views_ads_times_5: Optional["string"] = None
	views_ads_times_6: Optional["integer"] = None
	views_ads_times_7: Optional["integer"] = None
	views_ads_times_8: Optional["integer"] = None
	views_ads_times_9: Optional["integer"] = None
	views_ads_times_10: Optional["integer"] = None
	views_ads_times_11_plus: Optional["integer"] = None


class AdsTargSettings(AdsCriteria):
	"""VK Object AdsTargSettings

	id - Ad ID
	campaign_id - Campaign ID
	"""
	id = None
	campaign_id = None


class AdsTargStats(BaseModel):
	"""VK Object AdsTargStats

	audience_count - Audience
	recommended_cpc - Recommended CPC value for 50% reach (old format)
	recommended_cpm - Recommended CPM value for 50% reach (old format)
	recommended_cpc_50 - Recommended CPC value for 50% reach
	recommended_cpm_50 - Recommended CPM value for 50% reach
	recommended_cpc_70 - Recommended CPC value for 70% reach
	recommended_cpm_70 - Recommended CPM value for 70% reach
	recommended_cpc_90 - Recommended CPC value for 90% reach
	recommended_cpm_90 - Recommended CPM value for 90% reach
	"""
	audience_count: Optional["integer"] = None
	recommended_cpc: Optional["number"] = None
	recommended_cpm: Optional["number"] = None
	recommended_cpc_50: Optional["number"] = None
	recommended_cpm_50: Optional["number"] = None
	recommended_cpc_70: Optional["number"] = None
	recommended_cpm_70: Optional["number"] = None
	recommended_cpc_90: Optional["number"] = None
	recommended_cpm_90: Optional["number"] = None


class AdsTargSuggestions(BaseModel):
	"""VK Object AdsTargSuggestions

	id - Object ID
	name - Object name
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class AdsTargSuggestionsCities(BaseModel):
	"""VK Object AdsTargSuggestionsCities

	id - Object ID
	name - Object name
	parent - Parent object
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	parent: Optional["string"] = None


class AdsTargSuggestionsRegions(BaseModel):
	"""VK Object AdsTargSuggestionsRegions

	id - Object ID
	name - Object name
	type - Object type
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	type: Optional["string"] = None


class AdsTargSuggestionsSchools(BaseModel):
	"""VK Object AdsTargSuggestionsSchools

	desc - Full school title
	id - School ID
	name - School title
	parent - City name
	type - 
	"""
	desc: Optional["string"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None
	parent: Optional["string"] = None
	type: Optional["adstargsuggestionsschoolstype"] = None


class AdsTargSuggestionsSchoolsType(enum.Enum):
	"""VK Object AdsTargSuggestionsSchoolsType

	"""
	SCHOOL = "school"
	UNIVERSITY = "university"
	FACULTY = "faculty"
	CHAIR = "chair"


class AdsTargetGroup(BaseModel):
	"""VK Object AdsTargetGroup

	audience_count - Audience
	domain - Site domain
	id - Group ID
	lifetime - Number of days for user to be in group
	name - Group name
	pixel - Pixel code
	"""
	audience_count: Optional["integer"] = None
	domain: Optional["string"] = None
	id: Optional["integer"] = None
	lifetime: Optional["integer"] = None
	name: Optional["string"] = None
	pixel: Optional["string"] = None


class AdsUpdateofficeusersResult(BaseModel):
	"""VK Object AdsUpdateofficeusersResult

	"""
	user_id: Optional["integer"] = None
	is_success: Optional["boolean"] = None
	error: Optional["baseerror"] = None


class AdsUserSpecification(BaseModel):
	"""VK Object AdsUserSpecification

	"""
	user_id: Optional["integer"] = None
	role: Optional["adsaccessrolepublic"] = None
	grant_access_to_all_clients: Optional["boolean"] = None
	client_ids: Optional["integer"] = None
	view_budget: Optional["boolean"] = None


class AdsUserSpecificationCutted(BaseModel):
	"""VK Object AdsUserSpecificationCutted

	"""
	user_id: Optional["integer"] = None
	role: Optional["adsaccessrolepublic"] = None
	client_id: Optional["integer"] = None
	view_budget: Optional["boolean"] = None


class AdsUsers(BaseModel):
	"""VK Object AdsUsers

	accesses - 
	user_id - User ID
	"""
	accesses: Optional["adsaccesses"] = None
	user_id: Optional["integer"] = None


class AdswebGetadcategoriesResponseCategoriesCategory(BaseModel):
	"""VK Object AdswebGetadcategoriesResponseCategoriesCategory

	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class AdswebGetadunitsResponseAdUnitsAdUnit(BaseModel):
	"""VK Object AdswebGetadunitsResponseAdUnitsAdUnit

	"""
	id: Optional["integer"] = None
	site_id: Optional["integer"] = None
	name: Optional["string"] = None


class AdswebGetfraudhistoryResponseEntriesEntry(BaseModel):
	"""VK Object AdswebGetfraudhistoryResponseEntriesEntry

	"""
	site_id: Optional["integer"] = None
	day: Optional["string"] = None


class AdswebGetsitesResponseSitesSite(BaseModel):
	"""VK Object AdswebGetsitesResponseSitesSite

	"""
	id: Optional["integer"] = None
	status_user: Optional["string"] = None
	status_moder: Optional["string"] = None
	domains: Optional["string"] = None


class AdswebGetstatisticsResponseItemsItem(BaseModel):
	"""VK Object AdswebGetstatisticsResponseItemsItem

	"""
	site_id: Optional["integer"] = None
	ad_unit_id: Optional["integer"] = None
	overall_count: Optional["integer"] = None
	months_count: Optional["integer"] = None
	month_min: Optional["string"] = None
	month_max: Optional["string"] = None
	days_count: Optional["integer"] = None
	day_min: Optional["string"] = None
	day_max: Optional["string"] = None
	hours_count: Optional["integer"] = None
	hour_min: Optional["string"] = None
	hour_max: Optional["string"] = None


class AppWidgetsPhoto(BaseModel):
	"""VK Object AppWidgetsPhoto

	id - Image ID
	images - 
	"""
	id: Optional["string"] = None
	images: Optional["baseimage"] = None


class AppWidgetsPhotos(BaseModel):
	"""VK Object AppWidgetsPhotos

	"""
	count: Optional["integer"] = None
	items: Optional["appwidgetsphoto"] = None


class AppsApp(AppsAppMin):
	"""VK Object AppsApp

	author_url - Application author's URL
	banner_1120 - URL of the app banner with 1120 px in width
	banner_560 - URL of the app banner with 560 px in width
	icon_16 - URL of the app icon with 16 px in width
	is_new - Is new flag
	push_enabled - Is push enabled
	screen_orientation - Screen orientation
	friends - 
	catalog_position - Catalog position
	description - Application description
	genre - Genre name
	genre_id - Genre ID
	international - Information whether the application is multilanguage
	is_in_catalog - Information whether application is in mobile catalog
	leaderboard_type - 
	members_count - Members number
	platform_id - Application ID in store
	published_date - Date when the application has been published in Unixtime
	screen_name - Screen name
	section - Application section name
	"""
	author_url = None
	banner_1120 = None
	banner_560 = None
	icon_16 = None
	is_new = None
	push_enabled = None
	screen_orientation = None
	friends = None
	catalog_position = None
	description = None
	genre = None
	genre_id = None
	international = None
	is_in_catalog = None
	leaderboard_type = None
	members_count = None
	platform_id = None
	published_date = None
	screen_name = None
	section = None


class AppsAppLeaderboardType(enum.IntEnum):
	"""VK Object AppsAppLeaderboardType

	"""
	not supported = 0
	levels = 1
	points = 2


class AppsAppMin(BaseModel):
	"""VK Object AppsAppMin

	type - 
	id - Application ID
	title - Application title
	author_owner_id - Application author's ID
	is_installed - Is application installed
	icon_139 - URL of the app icon with 139 px in width
	icon_150 - URL of the app icon with 150 px in width
	icon_278 - URL of the app icon with 278 px in width
	icon_576 - URL of the app icon with 576 px in width
	background_loader_color - Hex color code without hash sign
	loader_icon - SVG data
	icon_75 - URL of the app icon with 75 px in width
	"""
	type: Optional["appsapptype"] = None
	id: Optional["integer"] = None
	title: Optional["string"] = None
	author_owner_id: Optional["integer"] = None
	is_installed: Optional["boolean"] = None
	icon_139: Optional["string"] = None
	icon_150: Optional["string"] = None
	icon_278: Optional["string"] = None
	icon_576: Optional["string"] = None
	background_loader_color: Optional["string"] = None
	loader_icon: Optional["string"] = None
	icon_75: Optional["string"] = None


class AppsAppType(enum.Enum):
	"""VK Object AppsAppType

	"""
	APP = "app"
	GAME = "game"
	SITE = "site"
	STANDALONE = "standalone"
	VK_APP = "vk_app"
	COMMUNITY_APP = "community_app"
	HTML5_GAME = "html5_game"
	MINI_APP = "mini_app"


class AppsLeaderboard(BaseModel):
	"""VK Object AppsLeaderboard

	level - Level
	points - Points number
	score - Score number
	user_id - User ID
	"""
	level: Optional["integer"] = None
	points: Optional["integer"] = None
	score: Optional["integer"] = None
	user_id: Optional["integer"] = None


class AppsScope(BaseModel):
	"""VK Object AppsScope

	name - Scope name
	title - Scope title
	"""
	name: Optional["string"] = None
	title: Optional["string"] = None


class AudioAudio(BaseModel):
	"""VK Object AudioAudio

	access_key - Access key for the audio
	artist - Artist name
	id - Audio ID
	owner_id - Audio owner's ID
	title - Title
	url - URL of mp3 file
	duration - Duration in seconds
	date - Date when uploaded
	album_id - Album ID
	genre_id - Genre ID
	performer - Performer name
	"""
	access_key: Optional["string"] = None
	artist: Optional["string"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	title: Optional["string"] = None
	url: Optional["string"] = None
	duration: Optional["integer"] = None
	date: Optional["integer"] = None
	album_id: Optional["integer"] = None
	genre_id: Optional["integer"] = None
	performer: Optional["string"] = None


class BaseBoolInt(enum.IntEnum):
	"""VK Object BaseBoolInt

	"""
	no = 0
	yes = 1


class BaseCity(BaseModel):
	"""VK Object BaseCity

	id - City ID
	title - City title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class BaseCommentsInfo(BaseModel):
	"""VK Object BaseCommentsInfo

	can_post - Information whether current user can comment the post
	count - Comments number
	groups_can_post - Information whether groups can comment the post
	donut - 
	"""
	can_post: Optional["baseboolint"] = None
	count: Optional["integer"] = None
	groups_can_post: Optional["boolean"] = None
	donut: Optional["wallwallpostcommentsdonut"] = None


class BaseCountry(BaseModel):
	"""VK Object BaseCountry

	id - Country ID
	title - Country title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class BaseCropPhoto(BaseModel):
	"""VK Object BaseCropPhoto

	"""
	photo: Optional["photosphoto"] = None
	crop: Optional["basecropphotocrop"] = None
	rect: Optional["basecropphotorect"] = None


class BaseCropPhotoCrop(BaseModel):
	"""VK Object BaseCropPhotoCrop

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x: Optional["number"] = None
	y: Optional["number"] = None
	x2: Optional["number"] = None
	y2: Optional["number"] = None


class BaseCropPhotoRect(BaseModel):
	"""VK Object BaseCropPhotoRect

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x: Optional["number"] = None
	y: Optional["number"] = None
	x2: Optional["number"] = None
	y2: Optional["number"] = None


class BaseError(BaseModel):
	"""VK Object BaseError

	error_code - Error code
	error_subcode - Error subcode
	error_msg - Error message
	error_text - Localized error message
	request_params - 
	"""
	error_code: Optional["integer"] = None
	error_subcode: Optional["integer"] = None
	error_msg: Optional["string"] = None
	error_text: Optional["string"] = None
	request_params: Optional["baserequestparam"] = None


class BaseGeo(BaseModel):
	"""VK Object BaseGeo

	coordinates - 
	place - 
	showmap - Information whether a map is showed
	type - Place type
	"""
	coordinates: Optional["basegeocoordinates"] = None
	place: Optional["baseplace"] = None
	showmap: Optional["integer"] = None
	type: Optional["string"] = None


class BaseGeoCoordinates(BaseModel):
	"""VK Object BaseGeoCoordinates

	"""
	latitude: Optional["number"] = None
	longitude: Optional["number"] = None


class BaseGradientPoint(BaseModel):
	"""VK Object BaseGradientPoint

	color - Hex color code without #
	position - Point position
	"""
	color: Optional["string"] = None
	position: Optional["number"] = None


class BaseImage(BaseModel):
	"""VK Object BaseImage

	id - 
	height - Image height
	url - Image url
	width - Image width
	"""
	id: Optional["string"] = None
	height: Optional["integer"] = None
	url: Optional["string"] = None
	width: Optional["integer"] = None


class BaseLikes(BaseModel):
	"""VK Object BaseLikes

	count - Likes number
	user_likes - Information whether current user likes the photo
	"""
	count: Optional["integer"] = None
	user_likes: Optional["baseboolint"] = None


class BaseLikesInfo(BaseModel):
	"""VK Object BaseLikesInfo

	can_like - Information whether current user can like the post
	can_publish - Information whether current user can repost
	count - Likes number
	user_likes - Information whether current uer has liked the post
	"""
	can_like: Optional["baseboolint"] = None
	can_publish: Optional["baseboolint"] = None
	count: Optional["integer"] = None
	user_likes: Optional["integer"] = None


class BaseLink(BaseModel):
	"""VK Object BaseLink

	application - 
	button - 
	caption - Link caption
	description - Link description
	id - Link ID
	is_favorite - 
	photo - 
	preview_page - String ID of the page with article preview
	preview_url - URL of the page with article preview
	product - 
	rating - 
	title - Link title
	url - Link URL
	target_object - 
	is_external - Information whether the current link is external
	video - Video from link
	"""
	application: Optional["baselinkapplication"] = None
	button: Optional["baselinkbutton"] = None
	caption: Optional["string"] = None
	description: Optional["string"] = None
	id: Optional["string"] = None
	is_favorite: Optional["boolean"] = None
	photo: Optional["photosphoto"] = None
	preview_page: Optional["string"] = None
	preview_url: Optional["string"] = None
	product: Optional["baselinkproduct"] = None
	rating: Optional["baselinkrating"] = None
	title: Optional["string"] = None
	url: Optional["string"] = None
	target_object: Optional["linktargetobject"] = None
	is_external: Optional["boolean"] = None
	video: Optional["videovideo"] = None


class BaseLinkApplication(BaseModel):
	"""VK Object BaseLinkApplication

	app_id - Application Id
	store - 
	"""
	app_id: Optional["number"] = None
	store: Optional["baselinkapplicationstore"] = None


class BaseLinkApplicationStore(BaseModel):
	"""VK Object BaseLinkApplicationStore

	id - Store Id
	name - Store name
	"""
	id: Optional["number"] = None
	name: Optional["string"] = None


class BaseLinkButton(BaseModel):
	"""VK Object BaseLinkButton

	action - Button action
	title - Button title
	block_id - Target block id
	section_id - Target section id
	curator_id - curator id
	owner_id - Owner id
	icon - Button icon name, e.g. 'phone' or 'gift'
	style - 
	"""
	action: Optional["baselinkbuttonaction"] = None
	title: Optional["string"] = None
	block_id: Optional["string"] = None
	section_id: Optional["string"] = None
	curator_id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	icon: Optional["string"] = None
	style: Optional["baselinkbuttonstyle"] = None


class BaseLinkButtonAction(BaseModel):
	"""VK Object BaseLinkButtonAction

	type - 
	url - Action URL
	consume_reason - 
	"""
	type: Optional["baselinkbuttonactiontype"] = None
	url: Optional["string"] = None
	consume_reason: Optional["string"] = None


class BaseLinkButtonActionType(enum.Enum):
	"""VK Object BaseLinkButtonActionType

	"""
	OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
	"""VK Object BaseLinkButtonStyle

	"""
	PRIMARY = "primary"
	SECONDARY = "secondary"


class BaseLinkProduct(BaseModel):
	"""VK Object BaseLinkProduct

	"""
	price: Optional["marketprice"] = None
	merchant: Optional["string"] = None
	orders_count: Optional["integer"] = None


class BaseLinkProductStatus(enum.Enum):
	"""VK Object BaseLinkProductStatus

	"""
	ACTIVE = "active"
	BLOCKED = "blocked"
	SOLD = "sold"
	DELETED = "deleted"
	ARCHIVED = "archived"


class BaseLinkRating(BaseModel):
	"""VK Object BaseLinkRating

	reviews_count - Count of reviews
	stars - Count of stars
	"""
	reviews_count: Optional["integer"] = None
	stars: Optional["number"] = None


class BaseMessageError(BaseModel):
	"""VK Object BaseMessageError

	code - Error code
	description - Error message
	"""
	code: Optional["integer"] = None
	description: Optional["string"] = None


class BaseObject(BaseModel):
	"""VK Object BaseObject

	id - Object ID
	title - Object title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class BaseObjectCount(BaseModel):
	"""VK Object BaseObjectCount

	count - Items count
	"""
	count: Optional["integer"] = None


class BaseObjectWithName(BaseModel):
	"""VK Object BaseObjectWithName

	id - Object ID
	name - Object name
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class BasePlace(BaseModel):
	"""VK Object BasePlace

	address - Place address
	checkins - Checkins number
	city - City name
	country - Country name
	created - Date of the place creation in Unixtime
	icon - URL of the place's icon
	id - Place ID
	latitude - Place latitude
	longitude - Place longitude
	title - Place title
	type - Place type
	"""
	address: Optional["string"] = None
	checkins: Optional["integer"] = None
	city: Optional["string"] = None
	country: Optional["string"] = None
	created: Optional["integer"] = None
	icon: Optional["string"] = None
	id: Optional["integer"] = None
	latitude: Optional["number"] = None
	longitude: Optional["number"] = None
	title: Optional["string"] = None
	type: Optional["string"] = None


class BasePropertyExists(enum.IntEnum):
	"""VK Object BasePropertyExists

	"""
	Property exists = 1


class BaseRepostsInfo(BaseModel):
	"""VK Object BaseRepostsInfo

	count - Total reposts counter. Sum of wall and mail reposts counters
	wall_count - Wall reposts counter
	mail_count - Mail reposts counter
	user_reposted - Information whether current user has reposted the post
	"""
	count: Optional["integer"] = None
	wall_count: Optional["integer"] = None
	mail_count: Optional["integer"] = None
	user_reposted: Optional["integer"] = None


class BaseRequestParam(BaseModel):
	"""VK Object BaseRequestParam

	key - Parameter name
	value - Parameter value
	"""
	key: Optional["string"] = None
	value: Optional["string"] = None


class BaseSex(enum.IntEnum):
	"""VK Object BaseSex

	"""
	unknown = 0
	female = 1
	male = 2


class BaseSticker(BaseModel):
	"""VK Object BaseSticker

	sticker_id - Sticker ID
	product_id - Pack ID
	images - 
	images_with_background - 
	animation_url - URL of sticker animation script
	animations - Array of sticker animation script objects
	is_allowed - Information whether the sticker is allowed
	"""
	sticker_id: Optional["integer"] = None
	product_id: Optional["integer"] = None
	images: Optional["baseimage"] = None
	images_with_background: Optional["baseimage"] = None
	animation_url: Optional["string"] = None
	animations: Optional["basestickeranimation"] = None
	is_allowed: Optional["boolean"] = None


class BaseStickerAnimation(BaseModel):
	"""VK Object BaseStickerAnimation

	type - Type of animation script
	url - URL of animation script
	"""
	type: Optional["string"] = None
	url: Optional["string"] = None
None

class BaseUploadServer(BaseModel):
	"""VK Object BaseUploadServer

	upload_url - Upload URL
	"""
	upload_url: Optional["string"] = None


class BaseUserGroupFields(enum.Enum):
	"""VK Object BaseUserGroupFields

	"""
	ABOUT = "about"
	ACTION_BUTTON = "action_button"
	ACTIVITIES = "activities"
	ACTIVITY = "activity"
	ADDRESSES = "addresses"
	ADMIN_LEVEL = "admin_level"
	AGE_LIMITS = "age_limits"
	AUTHOR_ID = "author_id"
	BAN_INFO = "ban_info"
	BDATE = "bdate"
	BLACKLISTED = "blacklisted"
	BLACKLISTED_BY_ME = "blacklisted_by_me"
	BOOKS = "books"
	CAN_CREATE_TOPIC = "can_create_topic"
	CAN_MESSAGE = "can_message"
	CAN_POST = "can_post"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_SEE_AUDIO = "can_see_audio"
	CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
	CAN_UPLOAD_VIDEO = "can_upload_video"
	CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
	CAREER = "career"
	CITY = "city"
	COMMON_COUNT = "common_count"
	CONNECTIONS = "connections"
	CONTACTS = "contacts"
	COUNTERS = "counters"
	COUNTRY = "country"
	COVER = "cover"
	CROP_PHOTO = "crop_photo"
	DEACTIVATED = "deactivated"
	DESCRIPTION = "description"
	DOMAIN = "domain"
	EDUCATION = "education"
	EXPORTS = "exports"
	FINISH_DATE = "finish_date"
	FIXED_POST = "fixed_post"
	FOLLOWERS_COUNT = "followers_count"
	FRIEND_STATUS = "friend_status"
	GAMES = "games"
	HAS_MARKET_APP = "has_market_app"
	HAS_MOBILE = "has_mobile"
	HAS_PHOTO = "has_photo"
	HOME_TOWN = "home_town"
	ID = "id"
	INTERESTS = "interests"
	IS_ADMIN = "is_admin"
	IS_CLOSED = "is_closed"
	IS_FAVORITE = "is_favorite"
	IS_FRIEND = "is_friend"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	IS_MEMBER = "is_member"
	IS_MESSAGES_BLOCKED = "is_messages_blocked"
	CAN_SEND_NOTIFY = "can_send_notify"
	IS_SUBSCRIBED = "is_subscribed"
	LAST_SEEN = "last_seen"
	LINKS = "links"
	LISTS = "lists"
	MAIDEN_NAME = "maiden_name"
	MAIN_ALBUM_ID = "main_album_id"
	MAIN_SECTION = "main_section"
	MARKET = "market"
	MEMBER_STATUS = "member_status"
	MEMBERS_COUNT = "members_count"
	MILITARY = "military"
	MOVIES = "movies"
	MUSIC = "music"
	NAME = "name"
	NICKNAME = "nickname"
	OCCUPATION = "occupation"
	ONLINE = "online"
	ONLINE_STATUS = "online_status"
	PERSONAL = "personal"
	PHONE = "phone"
	PHOTO_100 = "photo_100"
	PHOTO_200 = "photo_200"
	PHOTO_200_ORIG = "photo_200_orig"
	PHOTO_400_ORIG = "photo_400_orig"
	PHOTO_50 = "photo_50"
	PHOTO_ID = "photo_id"
	PHOTO_MAX = "photo_max"
	PHOTO_MAX_ORIG = "photo_max_orig"
	QUOTES = "quotes"
	RELATION = "relation"
	RELATIVES = "relatives"
	SCHOOLS = "schools"
	SCREEN_NAME = "screen_name"
	SEX = "sex"
	SITE = "site"
	START_DATE = "start_date"
	STATUS = "status"
	TIMEZONE = "timezone"
	TRENDING = "trending"
	TV = "tv"
	TYPE = "type"
	UNIVERSITIES = "universities"
	VERIFIED = "verified"
	WALL_COMMENTS = "wall_comments"
	WIKI_PAGE = "wiki_page"
	VK_ADMIN_STATUS = "vk_admin_status"


class BaseUserId(BaseModel):
	"""VK Object BaseUserId

	user_id - User ID
	"""
	user_id: Optional["integer"] = None


class BoardDefaultOrder(enum.IntEnum):
	"""VK Object BoardDefaultOrder

	"""
	desc_updated = 1
	desc_created = 2
	asc_updated = -1
	asc_created = -2


class BoardTopic(BaseModel):
	"""VK Object BoardTopic

	comments - Comments number
	created - Date when the topic has been created in Unixtime
	created_by - Creator ID
	id - Topic ID
	is_closed - Information whether the topic is closed
	is_fixed - Information whether the topic is fixed
	title - Topic title
	updated - Date when the topic has been updated in Unixtime
	updated_by - ID of user who updated the topic
	"""
	comments: Optional["integer"] = None
	created: Optional["integer"] = None
	created_by: Optional["integer"] = None
	id: Optional["integer"] = None
	is_closed: Optional["baseboolint"] = None
	is_fixed: Optional["baseboolint"] = None
	title: Optional["string"] = None
	updated: Optional["integer"] = None
	updated_by: Optional["integer"] = None


class BoardTopicComment(BaseModel):
	"""VK Object BoardTopicComment

	attachments - 
	date - Date when the comment has been added in Unixtime
	from_id - Author ID
	id - Comment ID
	real_offset - Real position of the comment
	text - Comment text
	can_edit - Information whether current user can edit the comment
	likes - 
	"""
	attachments: Optional["wallcommentattachment"] = None
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	id: Optional["integer"] = None
	real_offset: Optional["integer"] = None
	text: Optional["string"] = None
	can_edit: Optional["baseboolint"] = None
	likes: Optional["baselikesinfo"] = None


class BoardTopicPoll(BaseModel):
	"""VK Object BoardTopicPoll

	owner_id - Poll owner's ID
	poll_id - Poll ID
	created - Date when poll has been created in Unixtime
	is_closed - Information whether the poll is closed
	question - Poll question
	votes - Votes number
	answer_id - Current user's answer ID
	answers - 
	"""
	owner_id: Optional["integer"] = None
	poll_id: Optional["integer"] = None
	created: Optional["integer"] = None
	is_closed: Optional["baseboolint"] = None
	question: Optional["string"] = None
	votes: Optional["integer"] = None
	answer_id: Optional["integer"] = None
	answers: Optional["pollsanswer"] = None


class CallbackBoardPostDelete(BaseModel):
	"""VK Object CallbackBoardPostDelete

	"""
	topic_owner_id: Optional["integer"] = None
	topic_id: Optional["integer"] = None
	id: Optional["integer"] = None


class CallbackConfirmationMessage(BaseModel):
	"""VK Object CallbackConfirmationMessage

	"""
	type: Optional["callbackmessagetype"] = None
	group_id: Optional["integer"] = None
	secret: Optional["string"] = None


class CallbackDonutMoneyWithdraw(BaseModel):
	"""VK Object CallbackDonutMoneyWithdraw

	"""
	amount: Optional["number"] = None
	amount_without_fee: Optional["number"] = None


class CallbackDonutMoneyWithdrawError(BaseModel):
	"""VK Object CallbackDonutMoneyWithdrawError

	"""
	reason: Optional["string"] = None


class CallbackDonutSubscriptionCancelled(BaseModel):
	"""VK Object CallbackDonutSubscriptionCancelled

	"""
	user_id: Optional["integer"] = None


class CallbackDonutSubscriptionCreate(BaseModel):
	"""VK Object CallbackDonutSubscriptionCreate

	"""
	user_id: Optional["integer"] = None
	amount: Optional["integer"] = None
	amount_without_fee: Optional["number"] = None


class CallbackDonutSubscriptionExpired(BaseModel):
	"""VK Object CallbackDonutSubscriptionExpired

	"""
	user_id: Optional["integer"] = None


class CallbackDonutSubscriptionPriceChanged(BaseModel):
	"""VK Object CallbackDonutSubscriptionPriceChanged

	"""
	user_id: Optional["integer"] = None
	amount_old: Optional["integer"] = None
	amount_new: Optional["integer"] = None
	amount_diff: Optional["number"] = None
	amount_diff_without_fee: Optional["number"] = None


class CallbackDonutSubscriptionProlonged(BaseModel):
	"""VK Object CallbackDonutSubscriptionProlonged

	"""
	user_id: Optional["integer"] = None
	amount: Optional["integer"] = None
	amount_without_fee: Optional["number"] = None


class CallbackGroupChangePhoto(BaseModel):
	"""VK Object CallbackGroupChangePhoto

	"""
	user_id: Optional["integer"] = None
	photo: Optional["photosphoto"] = None


class CallbackGroupChangeSettings(BaseModel):
	"""VK Object CallbackGroupChangeSettings

	"""
	user_id: Optional["integer"] = None
	self: Optional["baseboolint"] = None


class CallbackGroupJoin(BaseModel):
	"""VK Object CallbackGroupJoin

	"""
	user_id: Optional["integer"] = None
	join_type: Optional["callbackgroupjointype"] = None


class CallbackGroupJoinType(enum.Enum):
	"""VK Object CallbackGroupJoinType

	"""
	JOIN = "join"
	UNSURE = "unsure"
	ACCEPTED = "accepted"
	APPROVED = "approved"
	REQUEST = "request"


class CallbackGroupLeave(BaseModel):
	"""VK Object CallbackGroupLeave

	"""
	user_id: Optional["integer"] = None
	self: Optional["baseboolint"] = None


class CallbackGroupMarket(enum.IntEnum):
	"""VK Object CallbackGroupMarket

	"""
	disabled = 0
	open = 1


class CallbackGroupOfficerRole(enum.IntEnum):
	"""VK Object CallbackGroupOfficerRole

	"""
	none = 0
	moderator = 1
	editor = 2
	administrator = 3


class CallbackGroupOfficersEdit(BaseModel):
	"""VK Object CallbackGroupOfficersEdit

	"""
	admin_id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	level_old: Optional["callbackgroupofficerrole"] = None
	level_new: Optional["callbackgroupofficerrole"] = None


class CallbackGroupSettingsChanges(BaseModel):
	"""VK Object CallbackGroupSettingsChanges

	"""
	title: Optional["string"] = None
	description: Optional["string"] = None
	access: Optional["groupsgroupisclosed"] = None
	screen_name: Optional["string"] = None
	public_category: Optional["integer"] = None
	public_subcategory: Optional["integer"] = None
	age_limits: Optional["groupsgroupfullagelimits"] = None
	website: Optional["string"] = None
	enable_status_default: Optional["groupsgroupwall"] = None
	enable_audio: Optional["groupsgroupaudio"] = None
	enable_video: Optional["groupsgroupvideo"] = None
	enable_photo: Optional["groupsgroupphotos"] = None
	enable_market: Optional["callbackgroupmarket"] = None


class CallbackLikeAddRemove(BaseModel):
	"""VK Object CallbackLikeAddRemove

	"""
	liker_id: Optional["integer"] = None
	object_type: Optional["string"] = None
	object_owner_id: Optional["integer"] = None
	object_id: Optional["integer"] = None
	post_id: Optional["integer"] = None
	thread_reply_id: Optional["integer"] = None


class CallbackMarketComment(BaseModel):
	"""VK Object CallbackMarketComment

	"""
	id: Optional["integer"] = None
	from_id: Optional["integer"] = None
	date: Optional["integer"] = None
	text: Optional["string"] = None
	market_owner_id: Optional["integer"] = None
	photo_id: Optional["integer"] = None


class CallbackMarketCommentDelete(BaseModel):
	"""VK Object CallbackMarketCommentDelete

	"""
	owner_id: Optional["integer"] = None
	id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	item_id: Optional["integer"] = None


class CallbackMessageAllow(BaseModel):
	"""VK Object CallbackMessageAllow

	"""
	user_id: Optional["integer"] = None
	key: Optional["string"] = None


class CallbackMessageBase(BaseModel):
	"""VK Object CallbackMessageBase

	"""
	type: Optional["callbackmessagetype"] = None
	object: Optional["object"] = None
	group_id: Optional["integer"] = None


class CallbackMessageDeny(BaseModel):
	"""VK Object CallbackMessageDeny

	"""
	user_id: Optional["integer"] = None


class CallbackMessageType(enum.Enum):
	"""VK Object CallbackMessageType

	"""
	AUDIO_NEW = "audio_new"
	BOARD_POST_NEW = "board_post_new"
	BOARD_POST_EDIT = "board_post_edit"
	BOARD_POST_RESTORE = "board_post_restore"
	BOARD_POST_DELETE = "board_post_delete"
	CONFIRMATION = "confirmation"
	GROUP_LEAVE = "group_leave"
	GROUP_JOIN = "group_join"
	GROUP_CHANGE_PHOTO = "group_change_photo"
	GROUP_CHANGE_SETTINGS = "group_change_settings"
	GROUP_OFFICERS_EDIT = "group_officers_edit"
	LEAD_FORMS_NEW = "lead_forms_new"
	MARKET_COMMENT_NEW = "market_comment_new"
	MARKET_COMMENT_DELETE = "market_comment_delete"
	MARKET_COMMENT_EDIT = "market_comment_edit"
	MARKET_COMMENT_RESTORE = "market_comment_restore"
	MESSAGE_ALLOW = "message_allow"
	MESSAGE_NEW = "message_new"
	MESSAGE_DENY = "message_deny"
	MESSAGE_READ = "message_read"
	MESSAGE_REPLY = "message_reply"
	MESSAGE_EDIT = "message_edit"
	MESSAGE_TYPING_STATE = "message_typing_state"
	MESSAGES_EDIT = "messages_edit"
	PHOTO_NEW = "photo_new"
	PHOTO_COMMENT_NEW = "photo_comment_new"
	PHOTO_COMMENT_DELETE = "photo_comment_delete"
	PHOTO_COMMENT_EDIT = "photo_comment_edit"
	PHOTO_COMMENT_RESTORE = "photo_comment_restore"
	POLL_VOTE_NEW = "poll_vote_new"
	USER_BLOCK = "user_block"
	USER_UNBLOCK = "user_unblock"
	VIDEO_NEW = "video_new"
	VIDEO_COMMENT_NEW = "video_comment_new"
	VIDEO_COMMENT_DELETE = "video_comment_delete"
	VIDEO_COMMENT_EDIT = "video_comment_edit"
	VIDEO_COMMENT_RESTORE = "video_comment_restore"
	WALL_POST_NEW = "wall_post_new"
	WALL_REPLY_NEW = "wall_reply_new"
	WALL_REPLY_EDIT = "wall_reply_edit"
	WALL_REPLY_DELETE = "wall_reply_delete"
	WALL_REPLY_RESTORE = "wall_reply_restore"
	WALL_REPOST = "wall_repost"


class CallbackPhotoComment(BaseModel):
	"""VK Object CallbackPhotoComment

	"""
	id: Optional["integer"] = None
	from_id: Optional["integer"] = None
	date: Optional["integer"] = None
	text: Optional["string"] = None
	photo_owner_id: Optional["integer"] = None


class CallbackPhotoCommentDelete(BaseModel):
	"""VK Object CallbackPhotoCommentDelete

	"""
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	photo_id: Optional["integer"] = None


class CallbackPollVoteNew(BaseModel):
	"""VK Object CallbackPollVoteNew

	"""
	owner_id: Optional["integer"] = None
	poll_id: Optional["integer"] = None
	option_id: Optional["integer"] = None
	user_id: Optional["integer"] = None


class CallbackQrScan(BaseModel):
	"""VK Object CallbackQrScan

	"""
	user_id: Optional["integer"] = None
	data: Optional["string"] = None
	type: Optional["string"] = None
	subtype: Optional["string"] = None
	reread: Optional["boolean"] = None


class CallbackUserBlock(BaseModel):
	"""VK Object CallbackUserBlock

	"""
	admin_id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	unblock_date: Optional["integer"] = None
	reason: Optional["integer"] = None
	comment: Optional["string"] = None


class CallbackUserUnblock(BaseModel):
	"""VK Object CallbackUserUnblock

	"""
	admin_id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	by_end_date: Optional["integer"] = None


class CallbackVideoComment(BaseModel):
	"""VK Object CallbackVideoComment

	"""
	id: Optional["integer"] = None
	from_id: Optional["integer"] = None
	date: Optional["integer"] = None
	text: Optional["string"] = None
	video_owner_id: Optional["integer"] = None


class CallbackVideoCommentDelete(BaseModel):
	"""VK Object CallbackVideoCommentDelete

	"""
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	video_id: Optional["integer"] = None


class CallbackWallCommentDelete(BaseModel):
	"""VK Object CallbackWallCommentDelete

	"""
	owner_id: Optional["integer"] = None
	id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	post_id: Optional["integer"] = None


class CallsCall(BaseModel):
	"""VK Object CallsCall

	duration - Call duration
	initiator_id - Caller initiator
	receiver_id - Caller receiver
	state - 
	time - Timestamp for call
	video - Was this call initiated as video call
	"""
	duration: Optional["integer"] = None
	initiator_id: Optional["integer"] = None
	receiver_id: Optional["integer"] = None
	state: Optional["callsendstate"] = None
	time: Optional["integer"] = None
	video: Optional["boolean"] = None


class CallsEndState(enum.Enum):
	"""VK Object CallsEndState

	"""
	CANCELED_BY_INITIATOR = "canceled_by_initiator"
	CANCELED_BY_RECEIVER = "canceled_by_receiver"
	REACHED = "reached"


class CallsParticipants(BaseModel):
	"""VK Object CallsParticipants

	list - 
	count - Participants count
	"""
	list: Optional["integer"] = None
	count: Optional["integer"] = None


class CommentThread(BaseModel):
	"""VK Object CommentThread

	can_post - Information whether current user can comment the post
	count - Comments number
	groups_can_post - Information whether groups can comment the post
	items - 
	show_reply_button - Information whether recommended to display reply button
	"""
	can_post: Optional["boolean"] = None
	count: Optional["integer"] = None
	groups_can_post: Optional["boolean"] = None
	items: Optional["wallwallcomment"] = None
	show_reply_button: Optional["boolean"] = None


class DatabaseCity(BaseObject):
	"""VK Object DatabaseCity

	area - Area title
	region - Region title
	important - Information whether the city is included in important cities list
	"""
	area = None
	region = None
	important = None


class DatabaseFaculty(BaseModel):
	"""VK Object DatabaseFaculty

	id - Faculty ID
	title - Faculty title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class DatabaseRegion(BaseModel):
	"""VK Object DatabaseRegion

	id - Region ID
	title - Region title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class DatabaseSchool(BaseModel):
	"""VK Object DatabaseSchool

	id - School ID
	title - School title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class DatabaseStation(BaseModel):
	"""VK Object DatabaseStation

	city_id - City ID
	color - Hex color code without #
	id - Station ID
	name - Station name
	"""
	city_id: Optional["integer"] = None
	color: Optional["string"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None


class DatabaseUniversity(BaseModel):
	"""VK Object DatabaseUniversity

	id - University ID
	title - University title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class DocsDoc(BaseModel):
	"""VK Object DocsDoc

	id - Document ID
	owner_id - Document owner ID
	title - Document title
	size - File size in bites
	ext - File extension
	url - File URL
	date - Date when file has been uploaded in Unixtime
	type - Document type
	preview - 
	is_licensed - 
	access_key - Access key for the document
	tags - Document tags
	"""
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	title: Optional["string"] = None
	size: Optional["integer"] = None
	ext: Optional["string"] = None
	url: Optional["string"] = None
	date: Optional["integer"] = None
	type: Optional["integer"] = None
	preview: Optional["docsdocpreview"] = None
	is_licensed: Optional["baseboolint"] = None
	access_key: Optional["string"] = None
	tags: Optional["string"] = None


class DocsDocAttachmentType(enum.Enum):
	"""VK Object DocsDocAttachmentType

	"""
	DOC = "doc"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
	"""VK Object DocsDocPreview

	"""
	audio_msg: Optional["docsdocpreviewaudiomsg"] = None
	graffiti: Optional["docsdocpreviewgraffiti"] = None
	photo: Optional["docsdocpreviewphoto"] = None
	video: Optional["docsdocpreviewvideo"] = None


class DocsDocPreviewAudioMsg(BaseModel):
	"""VK Object DocsDocPreviewAudioMsg

	duration - Audio message duration in seconds
	link_mp3 - MP3 file URL
	link_ogg - OGG file URL
	waveform - 
	"""
	duration: Optional["integer"] = None
	link_mp3: Optional["string"] = None
	link_ogg: Optional["string"] = None
	waveform: Optional["integer"] = None


class DocsDocPreviewGraffiti(BaseModel):
	"""VK Object DocsDocPreviewGraffiti

	src - Graffiti file URL
	width - Graffiti width
	height - Graffiti height
	"""
	src: Optional["string"] = None
	width: Optional["integer"] = None
	height: Optional["integer"] = None


class DocsDocPreviewPhoto(BaseModel):
	"""VK Object DocsDocPreviewPhoto

	"""
	sizes: Optional["docsdocpreviewphotosizes"] = None


class DocsDocPreviewPhotoSizes(BaseModel):
	"""VK Object DocsDocPreviewPhotoSizes

	src - URL of the image
	width - Width in px
	height - Height in px
	type - 
	"""
	src: Optional["string"] = None
	width: Optional["integer"] = None
	height: Optional["integer"] = None
	type: Optional["photosphotosizestype"] = None


class DocsDocPreviewVideo(BaseModel):
	"""VK Object DocsDocPreviewVideo

	src - Video URL
	width - Video's width in pixels
	height - Video's height in pixels
	file_size - Video file size in bites
	"""
	src: Optional["string"] = None
	width: Optional["integer"] = None
	height: Optional["integer"] = None
	file_size: Optional["integer"] = None


class DocsDocTypes(BaseModel):
	"""VK Object DocsDocTypes

	id - Doc type ID
	name - Doc type title
	count - Number of docs
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	count: Optional["integer"] = None


class DonutDonatorSubscriptionInfo(BaseModel):
	"""VK Object DonutDonatorSubscriptionInfo

	"""
	owner_id: Optional["integer"] = None
	next_payment_date: Optional["integer"] = None
	amount: Optional["integer"] = None
	status: Optional["string"] = None


class EventsEventAttach(BaseModel):
	"""VK Object EventsEventAttach

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	id - event ID
	is_favorite - is favorite
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address: Optional["string"] = None
	button_text: Optional["string"] = None
	friends: Optional["integer"] = None
	id: Optional["integer"] = None
	is_favorite: Optional["boolean"] = None
	member_status: Optional["groupsgroupfullmemberstatus"] = None
	text: Optional["string"] = None
	time: Optional["integer"] = None


class FaveBookmark(BaseModel):
	"""VK Object FaveBookmark

	added_date - Timestamp, when this item was bookmarked
	link - 
	post - 
	product - 
	seen - Has user seen this item
	tags - 
	type - Item type
	video - 
	"""
	added_date: Optional["integer"] = None
	link: Optional["baselink"] = None
	post: Optional["wallwallpostfull"] = None
	product: Optional["marketmarketitem"] = None
	seen: Optional["boolean"] = None
	tags: Optional["favetag"] = None
	type: Optional["favebookmarktype"] = None
	video: Optional["videovideo"] = None


class FaveBookmarkType(enum.Enum):
	"""VK Object FaveBookmarkType

	"""
	POST = "post"
	VIDEO = "video"
	PRODUCT = "product"
	ARTICLE = "article"
	LINK = "link"


class FavePage(BaseModel):
	"""VK Object FavePage

	description - Some info about user or group
	group - 
	tags - 
	type - Item type
	updated_date - Timestamp, when this page was bookmarked
	user - 
	"""
	description: Optional["string"] = None
	group: Optional["groupsgroupfull"] = None
	tags: Optional["favetag"] = None
	type: Optional["favepagetype"] = None
	updated_date: Optional["integer"] = None
	user: Optional["usersuserfull"] = None


class FavePageType(enum.Enum):
	"""VK Object FavePageType

	"""
	USER = "user"
	GROUP = "group"
	HINTS = "hints"


class FaveTag(BaseModel):
	"""VK Object FaveTag

	id - Tag id
	name - Tag name
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class FriendsFriendExtendedStatus(FriendsFriendStatus):
	"""VK Object FriendsFriendExtendedStatus

	is_request_unread - Is friend request from other user unread
	"""
	is_request_unread = None


class FriendsFriendStatus(BaseModel):
	"""VK Object FriendsFriendStatus

	friend_status - 
	sign - MD5 hash for the result validation
	user_id - User ID
	"""
	friend_status: Optional["friendsfriendstatusstatus"] = None
	sign: Optional["string"] = None
	user_id: Optional["integer"] = None


class FriendsFriendStatusStatus(enum.IntEnum):
	"""VK Object FriendsFriendStatusStatus

	"""
	not a friend = 0
	outcoming request = 1
	incoming request = 2
	is friend = 3


class FriendsFriendsList(BaseModel):
	"""VK Object FriendsFriendsList

	id - List ID
	name - List title
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class FriendsMutualFriend(BaseModel):
	"""VK Object FriendsMutualFriend

	common_count - Total mutual friends number
	common_friends - 
	id - User ID
	"""
	common_count: Optional["integer"] = None
	common_friends: Optional["integer"] = None
	id: Optional["integer"] = None


class FriendsRequests(BaseModel):
	"""VK Object FriendsRequests

	from - ID of the user by whom friend has been suggested
	mutual - 
	user_id - User ID
	"""
	from: Optional["string"] = None
	mutual: Optional["friendsrequestsmutual"] = None
	user_id: Optional["integer"] = None


class FriendsRequestsMutual(BaseModel):
	"""VK Object FriendsRequestsMutual

	count - Total mutual friends number
	users - 
	"""
	count: Optional["integer"] = None
	users: Optional["integer"] = None


class FriendsRequestsXtrMessage(BaseModel):
	"""VK Object FriendsRequestsXtrMessage

	from - ID of the user by whom friend has been suggested
	message - Message sent with a request
	mutual - 
	user_id - User ID
	"""
	from: Optional["string"] = None
	message: Optional["string"] = None
	mutual: Optional["friendsrequestsmutual"] = None
	user_id: Optional["integer"] = None


class FriendsUserXtrLists(UsersUserFull):
	"""VK Object FriendsUserXtrLists

	"""
	lists = None


class FriendsUserXtrPhone(UsersUserFull):
	"""VK Object FriendsUserXtrPhone

	phone - User phone
	"""
	phone = None


class GiftsGift(BaseModel):
	"""VK Object GiftsGift

	date - Date when gist has been sent in Unixtime
	from_id - Gift sender ID
	gift - 
	gift_hash - Hash
	id - Gift ID
	message - Comment text
	privacy - 
	"""
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	gift: Optional["giftslayout"] = None
	gift_hash: Optional["string"] = None
	id: Optional["integer"] = None
	message: Optional["string"] = None
	privacy: Optional["giftsgiftprivacy"] = None


class GiftsGiftPrivacy(enum.IntEnum):
	"""VK Object GiftsGiftPrivacy

	"""
	name and message for all = 0
	name for all = 1
	name and message for recipient only = 2


class GiftsLayout(BaseModel):
	"""VK Object GiftsLayout

	id - Gift ID
	thumb_512 - URL of the preview image with 512 px in width
	thumb_256 - URL of the preview image with 256 px in width
	thumb_48 - URL of the preview image with 48 px in width
	thumb_96 - URL of the preview image with 96 px in width
	stickers_product_id - ID of the sticker pack, if the gift is representing one
	is_stickers_style - Information whether gift represents a stickers style
	build_id - ID of the build of constructor gift
	keywords - Keywords used for search
	"""
	id: Optional["integer"] = None
	thumb_512: Optional["string"] = None
	thumb_256: Optional["string"] = None
	thumb_48: Optional["string"] = None
	thumb_96: Optional["string"] = None
	stickers_product_id: Optional["integer"] = None
	is_stickers_style: Optional["boolean"] = None
	build_id: Optional["string"] = None
	keywords: Optional["string"] = None


class GroupsAddress(BaseModel):
	"""VK Object GroupsAddress

	additional_address - Additional address to the place (6 floor, left door)
	address - String address to the place (Nevsky, 28)
	city_id - City id of address
	country_id - Country id of address
	distance - Distance from the point
	id - Address id
	latitude - Address latitude
	longitude - Address longitude
	metro_station_id - Metro id of address
	phone - Address phone
	time_offset - Time offset int minutes from utc time
	timetable - Week timetable for the address
	title - Title of the place (Zinger, etc)
	work_info_status - Status of information about timetable
	"""
	additional_address: Optional["string"] = None
	address: Optional["string"] = None
	city_id: Optional["integer"] = None
	country_id: Optional["integer"] = None
	distance: Optional["integer"] = None
	id: Optional["integer"] = None
	latitude: Optional["number"] = None
	longitude: Optional["number"] = None
	metro_station_id: Optional["integer"] = None
	phone: Optional["string"] = None
	time_offset: Optional["integer"] = None
	timetable: Optional["groupsaddresstimetable"] = None
	title: Optional["string"] = None
	work_info_status: Optional["groupsaddressworkinfostatus"] = None


class GroupsAddressTimetable(BaseModel):
	"""VK Object GroupsAddressTimetable

	fri - Timetable for friday
	mon - Timetable for monday
	sat - Timetable for saturday
	sun - Timetable for sunday
	thu - Timetable for thursday
	tue - Timetable for tuesday
	wed - Timetable for wednesday
	"""
	fri: Optional["groupsaddresstimetableday"] = None
	mon: Optional["groupsaddresstimetableday"] = None
	sat: Optional["groupsaddresstimetableday"] = None
	sun: Optional["groupsaddresstimetableday"] = None
	thu: Optional["groupsaddresstimetableday"] = None
	tue: Optional["groupsaddresstimetableday"] = None
	wed: Optional["groupsaddresstimetableday"] = None


class GroupsAddressTimetableDay(BaseModel):
	"""VK Object GroupsAddressTimetableDay

	break_close_time - Close time of the break in minutes
	break_open_time - Start time of the break in minutes
	close_time - Close time in minutes
	open_time - Open time in minutes
	"""
	break_close_time: Optional["integer"] = None
	break_open_time: Optional["integer"] = None
	close_time: Optional["integer"] = None
	open_time: Optional["integer"] = None


class GroupsAddressWorkInfoStatus(enum.Enum):
	"""VK Object GroupsAddressWorkInfoStatus

	"""
	NO_INFORMATION = "no_information"
	TEMPORARILY_CLOSED = "temporarily_closed"
	ALWAYS_OPENED = "always_opened"
	TIMETABLE = "timetable"
	FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
	"""VK Object GroupsAddressesInfo

	is_enabled - Information whether addresses is enabled
	main_address_id - Main address id for group
	"""
	is_enabled: Optional["boolean"] = None
	main_address_id: Optional["integer"] = None


class GroupsBanInfo(BaseModel):
	"""VK Object GroupsBanInfo

	admin_id - Administrator ID
	comment - Comment for a ban
	comment_visible - Show comment for user
	is_closed - 
	date - Date when user has been added to blacklist in Unixtime
	end_date - Date when user will be removed from blacklist in Unixtime
	reason - 
	"""
	admin_id: Optional["integer"] = None
	comment: Optional["string"] = None
	comment_visible: Optional["boolean"] = None
	is_closed: Optional["boolean"] = None
	date: Optional["integer"] = None
	end_date: Optional["integer"] = None
	reason: Optional["groupsbaninforeason"] = None


class GroupsBanInfoReason(enum.IntEnum):
	"""VK Object GroupsBanInfoReason

	"""
	other = 0
	spam = 1
	verbal abuse = 2
	strong language = 3
	flood = 4


class GroupsBannedItem(BaseModel):
	"""VK Object GroupsBannedItem

	"""


class GroupsCallbackServer(BaseModel):
	"""VK Object GroupsCallbackServer

	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None
	creator_id: Optional["integer"] = None
	url: Optional["string"] = None
	secret_key: Optional["string"] = None
	status: Optional["string"] = None


class GroupsCallbackSettings(BaseModel):
	"""VK Object GroupsCallbackSettings

	api_version - API version used for the events
	events - 
	"""
	api_version: Optional["string"] = None
	events: Optional["groupslongpollevents"] = None


class GroupsContactsItem(BaseModel):
	"""VK Object GroupsContactsItem

	user_id - User ID
	desc - Contact description
	phone - Contact phone
	email - Contact email
	"""
	user_id: Optional["integer"] = None
	desc: Optional["string"] = None
	phone: Optional["string"] = None
	email: Optional["string"] = None


class GroupsCountersGroup(BaseModel):
	"""VK Object GroupsCountersGroup

	addresses - Addresses number
	albums - Photo albums number
	audios - Audios number
	audio_playlists - Audio playlists number
	docs - Docs number
	market - Market items number
	photos - Photos number
	topics - Topics number
	videos - Videos number
	"""
	addresses: Optional["integer"] = None
	albums: Optional["integer"] = None
	audios: Optional["integer"] = None
	audio_playlists: Optional["integer"] = None
	docs: Optional["integer"] = None
	market: Optional["integer"] = None
	photos: Optional["integer"] = None
	topics: Optional["integer"] = None
	videos: Optional["integer"] = None


class GroupsCover(BaseModel):
	"""VK Object GroupsCover

	enabled - Information whether cover is enabled
	images - 
	"""
	enabled: Optional["baseboolint"] = None
	images: Optional["baseimage"] = None


class GroupsFields(enum.Enum):
	"""VK Object GroupsFields

	"""
	MARKET = "market"
	MEMBER_STATUS = "member_status"
	IS_FAVORITE = "is_favorite"
	IS_SUBSCRIBED = "is_subscribed"
	IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
	CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
	CITY = "city"
	COUNTRY = "country"
	VERIFIED = "verified"
	DESCRIPTION = "description"
	WIKI_PAGE = "wiki_page"
	MEMBERS_COUNT = "members_count"
	REQUESTS_COUNT = "requests_count"
	COUNTERS = "counters"
	COVER = "cover"
	CAN_POST = "can_post"
	CAN_SUGGEST = "can_suggest"
	CAN_UPLOAD_STORY = "can_upload_story"
	CAN_UPLOAD_DOC = "can_upload_doc"
	CAN_UPLOAD_VIDEO = "can_upload_video"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_CREATE_TOPIC = "can_create_topic"
	ACTIVITY = "activity"
	FIXED_POST = "fixed_post"
	HAS_PHOTO = "has_photo"
	STATUS = "status"
	MAIN_ALBUM_ID = "main_album_id"
	LINKS = "links"
	CONTACTS = "contacts"
	SITE = "site"
	MAIN_SECTION = "main_section"
	SECONDARY_SECTION = "secondary_section"
	WALL = "wall"
	TRENDING = "trending"
	CAN_MESSAGE = "can_message"
	IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
	IS_MESSAGES_BLOCKED = "is_messages_blocked"
	CAN_SEND_NOTIFY = "can_send_notify"
	HAS_GROUP_CHANNEL = "has_group_channel"
	GROUP_CHANNEL = "group_channel"
	ONLINE_STATUS = "online_status"
	START_DATE = "start_date"
	FINISH_DATE = "finish_date"
	AGE_LIMITS = "age_limits"
	BAN_INFO = "ban_info"
	ACTION_BUTTON = "action_button"
	AUTHOR_ID = "author_id"
	PHONE = "phone"
	HAS_MARKET_APP = "has_market_app"
	ADDRESSES = "addresses"
	LIVE_COVERS = "live_covers"
	IS_ADULT = "is_adult"
	CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
	WARNING_NOTIFICATION = "warning_notification"
	MSG_PUSH_ALLOWED = "msg_push_allowed"
	STORIES_ARCHIVE_COUNT = "stories_archive_count"
	VIDEO_LIVE_LEVEL = "video_live_level"
	VIDEO_LIVE_COUNT = "video_live_count"
	CLIPS_COUNT = "clips_count"
	IS_BUSINESS = "is_business"


class GroupsFilter(enum.Enum):
	"""VK Object GroupsFilter

	"""
	ADMIN = "admin"
	EDITOR = "editor"
	MODER = "moder"
	ADVERTISER = "advertiser"
	GROUPS = "groups"
	PUBLICS = "publics"
	EVENTS = "events"
	HAS_ADDRESSES = "has_addresses"


class GroupsGroup(BaseModel):
	"""VK Object GroupsGroup

	id - Community ID
	name - Community name
	screen_name - Domain of the community page
	is_closed - 
	type - 
	is_admin - Information whether current user is administrator
	admin_level - 
	is_member - Information whether current user is member
	is_advertiser - Information whether current user is advertiser
	start_date - Start date in Unixtime format
	finish_date - Finish date in Unixtime format
	deactivated - Information whether community is banned
	photo_50 - URL of square photo of the community with 50 pixels in width
	photo_100 - URL of square photo of the community with 100 pixels in width
	photo_200 - URL of square photo of the community with 200 pixels in width
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	screen_name: Optional["string"] = None
	is_closed: Optional["groupsgroupisclosed"] = None
	type: Optional["groupsgrouptype"] = None
	is_admin: Optional["baseboolint"] = None
	admin_level: Optional["groupsgroupadminlevel"] = None
	is_member: Optional["baseboolint"] = None
	is_advertiser: Optional["baseboolint"] = None
	start_date: Optional["integer"] = None
	finish_date: Optional["integer"] = None
	deactivated: Optional["string"] = None
	photo_50: Optional["string"] = None
	photo_100: Optional["string"] = None
	photo_200: Optional["string"] = None


class GroupsGroupAccess(enum.IntEnum):
	"""VK Object GroupsGroupAccess

	"""
	open = 0
	closed = 1
	private = 2


class GroupsGroupAdminLevel(enum.IntEnum):
	"""VK Object GroupsGroupAdminLevel

	"""
	moderator = 1
	editor = 2
	administrator = 3


class GroupsGroupAgeLimits(enum.IntEnum):
	"""VK Object GroupsGroupAgeLimits

	"""
	unlimited = 1
	_16 plus = 2
	_18 plus = 3


class GroupsGroupAttach(BaseModel):
	"""VK Object GroupsGroupAttach

	id - group ID
	text - text of attach
	status - activity or category of group
	size - size of group
	is_favorite - is favorite
	"""
	id: Optional["integer"] = None
	text: Optional["string"] = None
	status: Optional["string"] = None
	size: Optional["integer"] = None
	is_favorite: Optional["boolean"] = None


class GroupsGroupAudio(enum.IntEnum):
	"""VK Object GroupsGroupAudio

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupBanInfo(BaseModel):
	"""VK Object GroupsGroupBanInfo

	comment - Ban comment
	end_date - End date of ban in Unixtime
	reason - 
	"""
	comment: Optional["string"] = None
	end_date: Optional["integer"] = None
	reason: Optional["groupsbaninforeason"] = None


class GroupsGroupCategory(BaseModel):
	"""VK Object GroupsGroupCategory

	id - Category ID
	name - Category name
	subcategories - 
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	subcategories: Optional["baseobjectwithname"] = None


class GroupsGroupCategoryFull(BaseModel):
	"""VK Object GroupsGroupCategoryFull

	id - Category ID
	name - Category name
	page_count - Pages number
	page_previews - 
	subcategories - 
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	page_count: Optional["integer"] = None
	page_previews: Optional["groupsgroup"] = None
	subcategories: Optional["groupsgroupcategory"] = None


class GroupsGroupCategoryType(BaseModel):
	"""VK Object GroupsGroupCategoryType

	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class GroupsGroupDocs(enum.IntEnum):
	"""VK Object GroupsGroupDocs

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupFull(GroupsGroup):
	"""VK Object GroupsGroupFull

	market - 
	member_status - Current user's member status
	is_adult - Information whether community is adult
	is_hidden_from_feed - Information whether community is hidden from current user's newsfeed
	is_favorite - Information whether community is in faves
	is_subscribed - Information whether current user is subscribed
	city - 
	country - 
	verified - Information whether community is verified
	description - Community description
	wiki_page - Community's main wiki page title
	members_count - Community members number
	requests_count - The number of incoming requests to the community
	video_live_level - Community level live streams achievements
	video_live_count - Number of community's live streams
	clips_count - Number of community's clips
	counters - 
	cover - 
	can_post - Information whether current user can post on community's wall
	can_suggest - 
	can_upload_story - Information whether current user can upload story
	can_upload_doc - Information whether current user can upload doc
	can_upload_video - Information whether current user can upload video
	can_see_all_posts - Information whether current user can see all posts on community's wall
	can_create_topic - Information whether current user can create topic
	activity - Type of group, start date of event or category of public page
	fixed_post - Fixed post ID
	has_photo - Information whether community has photo
	crop_photo - Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества
	status - Community status
	status_audio - 
	main_album_id - Community's main photo album ID
	links - 
	contacts - 
	wall - Information about wall status in community
	site - Community's website
	main_section - 
	secondary_section - 
	trending - Information whether the community has a "fire" pictogram.
	can_message - Information whether current user can send a message to community
	is_messages_blocked - Information whether community can send a message to current user
	can_send_notify - Information whether community can send notifications by phone number to current user
	online_status - Status of replies in community messages
	invited_by - Inviter ID
	age_limits - Information whether age limit
	ban_info - User ban info
	has_market_app - Information whether community has installed market app
	using_vkpay_market_app - 
	has_group_channel - 
	addresses - Info about addresses in groups
	is_subscribed_podcasts - Information whether current user is subscribed to podcasts
	can_subscribe_podcasts - Owner in whitelist or not
	can_subscribe_posts - Can subscribe to wall
	live_covers - Live covers state
	stories_archive_count - 
	"""
	market = None
	member_status = None
	is_adult = None
	is_hidden_from_feed = None
	is_favorite = None
	is_subscribed = None
	city = None
	country = None
	verified = None
	description = None
	wiki_page = None
	members_count = None
	requests_count = None
	video_live_level = None
	video_live_count = None
	clips_count = None
	counters = None
	cover = None
	can_post = None
	can_suggest = None
	can_upload_story = None
	can_upload_doc = None
	can_upload_video = None
	can_see_all_posts = None
	can_create_topic = None
	activity = None
	fixed_post = None
	has_photo = None
	crop_photo = None
	status = None
	status_audio = None
	main_album_id = None
	links = None
	contacts = None
	wall = None
	site = None
	main_section = None
	secondary_section = None
	trending = None
	can_message = None
	is_messages_blocked = None
	can_send_notify = None
	online_status = None
	invited_by = None
	age_limits = None
	ban_info = None
	has_market_app = None
	using_vkpay_market_app = None
	has_group_channel = None
	addresses = None
	is_subscribed_podcasts = None
	can_subscribe_podcasts = None
	can_subscribe_posts = None
	live_covers = None
	stories_archive_count = None


class GroupsGroupFullAgeLimits(enum.IntEnum):
	"""VK Object GroupsGroupFullAgeLimits

	"""
	no = 1
	over 16 = 2
	over 18 = 3


class GroupsGroupFullMainSection(enum.IntEnum):
	"""VK Object GroupsGroupFullMainSection

	"""
	absent = 0
	photos = 1
	topics = 2
	audio = 3
	video = 4
	market = 5


class GroupsGroupFullMemberStatus(enum.IntEnum):
	"""VK Object GroupsGroupFullMemberStatus

	"""
	not a member = 0
	member = 1
	not sure = 2
	declined = 3
	has sent a request = 4
	invited = 5


class GroupsGroupIsClosed(enum.IntEnum):
	"""VK Object GroupsGroupIsClosed

	"""
	open = 0
	closed = 1
	private = 2


class GroupsGroupLink(BaseModel):
	"""VK Object GroupsGroupLink

	name - Link label
	desc - Link description
	edit_title - Information whether the title can be edited
	id - Link ID
	image_processing - Information whether the image on processing
	url - Link URL
	"""
	name: Optional["string"] = None
	desc: Optional["string"] = None
	edit_title: Optional["baseboolint"] = None
	id: Optional["integer"] = None
	image_processing: Optional["baseboolint"] = None
	url: Optional["string"] = None


class GroupsGroupMarketCurrency(enum.IntEnum):
	"""VK Object GroupsGroupMarketCurrency

	"""
	russian rubles = 643
	ukrainian hryvnia = 980
	kazakh tenge = 398
	euro = 978
	us dollars = 840


class GroupsGroupPhotos(enum.IntEnum):
	"""VK Object GroupsGroupPhotos

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupPublicCategoryList(BaseModel):
	"""VK Object GroupsGroupPublicCategoryList

	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	subcategories: Optional["groupsgroupcategorytype"] = None


class GroupsGroupRole(enum.Enum):
	"""VK Object GroupsGroupRole

	"""
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	ADVERTISER = "advertiser"


class GroupsGroupSubject(enum.IntEnum):
	"""VK Object GroupsGroupSubject

	"""
	auto = 1
	activity holidays = 2
	business = 3
	pets = 4
	health = 5
	dating and communication = 6
	games = 7
	it = 8
	cinema = 9
	beauty and fashion = 10
	cooking = 11
	art and culture = 12
	literature = 13
	mobile services and internet = 14
	music = 15
	science and technology = 16
	real estate = 17
	news and media = 18
	security = 19
	education = 20
	home and renovations = 21
	politics = 22
	food = 23
	industry = 24
	travel = 25
	work = 26
	entertainment = 27
	religion = 28
	family = 29
	sports = 30
	insurance = 31
	television = 32
	goods and services = 33
	hobbies = 34
	finance = 35
	photo = 36
	esoterics = 37
	electronics and appliances = 38
	erotic = 39
	humor = 40
	society_humanities = 41
	design and graphics = 42


class GroupsGroupSuggestedPrivacy(enum.IntEnum):
	"""VK Object GroupsGroupSuggestedPrivacy

	"""
	none = 0
	all = 1
	subscribers = 2


class GroupsGroupTag(BaseModel):
	"""VK Object GroupsGroupTag

	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	color: Optional["string"] = None
	uses: Optional["integer"] = None


class GroupsGroupTopics(enum.IntEnum):
	"""VK Object GroupsGroupTopics

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupType(enum.Enum):
	"""VK Object GroupsGroupType

	"""
	GROUP = "group"
	PAGE = "page"
	EVENT = "event"


class GroupsGroupVideo(enum.IntEnum):
	"""VK Object GroupsGroupVideo

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupWall(enum.IntEnum):
	"""VK Object GroupsGroupWall

	"""
	disabled = 0
	open = 1
	limited = 2
	closed = 3


class GroupsGroupWiki(enum.IntEnum):
	"""VK Object GroupsGroupWiki

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupsArray(BaseModel):
	"""VK Object GroupsGroupsArray

	count - Communities number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["integer"] = None


class GroupsLinksItem(BaseModel):
	"""VK Object GroupsLinksItem

	desc - Link description
	edit_title - Information whether the link title can be edited
	id - Link ID
	name - Link title
	photo_100 - URL of square image of the link with 100 pixels in width
	photo_50 - URL of square image of the link with 50 pixels in width
	url - Link URL
	"""
	desc: Optional["string"] = None
	edit_title: Optional["baseboolint"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None
	photo_100: Optional["string"] = None
	photo_50: Optional["string"] = None
	url: Optional["string"] = None


class GroupsLiveCovers(BaseModel):
	"""VK Object GroupsLiveCovers

	is_enabled - Information whether live covers is enabled
	is_scalable - Information whether live covers photo scaling is enabled
	story_ids - 
	"""
	is_enabled: Optional["boolean"] = None
	is_scalable: Optional["boolean"] = None
	story_ids: Optional["string"] = None


class GroupsLongPollEvents(BaseModel):
	"""VK Object GroupsLongPollEvents

	"""
	audio_new: Optional["baseboolint"] = None
	board_post_delete: Optional["baseboolint"] = None
	board_post_edit: Optional["baseboolint"] = None
	board_post_new: Optional["baseboolint"] = None
	board_post_restore: Optional["baseboolint"] = None
	group_change_photo: Optional["baseboolint"] = None
	group_change_settings: Optional["baseboolint"] = None
	group_join: Optional["baseboolint"] = None
	group_leave: Optional["baseboolint"] = None
	group_officers_edit: Optional["baseboolint"] = None
	lead_forms_new: Optional["baseboolint"] = None
	market_comment_delete: Optional["baseboolint"] = None
	market_comment_edit: Optional["baseboolint"] = None
	market_comment_new: Optional["baseboolint"] = None
	market_comment_restore: Optional["baseboolint"] = None
	market_order_new: Optional["baseboolint"] = None
	market_order_edit: Optional["baseboolint"] = None
	message_allow: Optional["baseboolint"] = None
	message_deny: Optional["baseboolint"] = None
	message_new: Optional["baseboolint"] = None
	message_read: Optional["baseboolint"] = None
	message_reply: Optional["baseboolint"] = None
	message_typing_state: Optional["baseboolint"] = None
	message_edit: Optional["baseboolint"] = None
	photo_comment_delete: Optional["baseboolint"] = None
	photo_comment_edit: Optional["baseboolint"] = None
	photo_comment_new: Optional["baseboolint"] = None
	photo_comment_restore: Optional["baseboolint"] = None
	photo_new: Optional["baseboolint"] = None
	poll_vote_new: Optional["baseboolint"] = None
	user_block: Optional["baseboolint"] = None
	user_unblock: Optional["baseboolint"] = None
	video_comment_delete: Optional["baseboolint"] = None
	video_comment_edit: Optional["baseboolint"] = None
	video_comment_new: Optional["baseboolint"] = None
	video_comment_restore: Optional["baseboolint"] = None
	video_new: Optional["baseboolint"] = None
	wall_post_new: Optional["baseboolint"] = None
	wall_reply_delete: Optional["baseboolint"] = None
	wall_reply_edit: Optional["baseboolint"] = None
	wall_reply_new: Optional["baseboolint"] = None
	wall_reply_restore: Optional["baseboolint"] = None
	wall_repost: Optional["baseboolint"] = None
	donut_subscription_create: Optional["baseboolint"] = None
	donut_subscription_prolonged: Optional["baseboolint"] = None
	donut_subscription_cancelled: Optional["baseboolint"] = None
	donut_subscription_expired: Optional["baseboolint"] = None
	donut_subscription_price_changed: Optional["baseboolint"] = None
	donut_money_withdraw: Optional["baseboolint"] = None
	donut_money_withdraw_error: Optional["baseboolint"] = None


class GroupsLongPollServer(BaseModel):
	"""VK Object GroupsLongPollServer

	key - Long Poll key
	server - Long Poll server address
	ts - Number of the last event
	"""
	key: Optional["string"] = None
	server: Optional["string"] = None
	ts: Optional["string"] = None


class GroupsLongPollSettings(BaseModel):
	"""VK Object GroupsLongPollSettings

	api_version - API version used for the events
	events - 
	is_enabled - Shows whether Long Poll is enabled
	"""
	api_version: Optional["string"] = None
	events: Optional["groupslongpollevents"] = None
	is_enabled: Optional["boolean"] = None


class GroupsMarketInfo(BaseModel):
	"""VK Object GroupsMarketInfo

	contact_id - Contact person ID
	currency - 
	currency_text - Currency name
	enabled - Information whether the market is enabled
	main_album_id - Main market album ID
	price_max - Maximum price
	price_min - Minimum price
	"""
	contact_id: Optional["integer"] = None
	currency: Optional["marketcurrency"] = None
	currency_text: Optional["string"] = None
	enabled: Optional["baseboolint"] = None
	main_album_id: Optional["integer"] = None
	price_max: Optional["string"] = None
	price_min: Optional["string"] = None


class GroupsMarketState(enum.Enum):
	"""VK Object GroupsMarketState

	"""
	NONE = "none"
	BASIC = "basic"
	ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
	"""VK Object GroupsMemberRole

	id - User ID
	permissions - 
	role - 
	"""
	id: Optional["integer"] = None
	permissions: Optional["groupsmemberrolepermission"] = None
	role: Optional["groupsmemberrolestatus"] = None


class GroupsMemberRolePermission(enum.Enum):
	"""VK Object GroupsMemberRolePermission

	"""
	ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
	"""VK Object GroupsMemberRoleStatus

	"""
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	CREATOR = "creator"


class GroupsMemberStatus(BaseModel):
	"""VK Object GroupsMemberStatus

	member - Information whether user is a member of the group
	user_id - User ID
	"""
	member: Optional["baseboolint"] = None
	user_id: Optional["integer"] = None


class GroupsMemberStatusFull(BaseModel):
	"""VK Object GroupsMemberStatusFull

	can_invite - Information whether user can be invited
	can_recall - Information whether user's invite to the group can be recalled
	invitation - Information whether user has been invited to the group
	member - Information whether user is a member of the group
	request - Information whether user has send request to the group
	user_id - User ID
	"""
	can_invite: Optional["baseboolint"] = None
	can_recall: Optional["baseboolint"] = None
	invitation: Optional["baseboolint"] = None
	member: Optional["baseboolint"] = None
	request: Optional["baseboolint"] = None
	user_id: Optional["integer"] = None


class GroupsOnlineStatus(BaseModel):
	"""VK Object GroupsOnlineStatus

	minutes - Estimated time of answer (for status = answer_mark)
	status - 
	"""
	minutes: Optional["integer"] = None
	status: Optional["groupsonlinestatustype"] = None


class GroupsOnlineStatusType(enum.Enum):
	"""VK Object GroupsOnlineStatusType

	"""
	NONE = "none"
	ONLINE = "online"
	ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(BaseModel):
	"""VK Object GroupsOwnerXtrBanInfo

	ban_info - 
	group - Information about group if type = group
	profile - Information about group if type = profile
	type - 
	"""
	ban_info: Optional["groupsbaninfo"] = None
	group: Optional["groupsgroup"] = None
	profile: Optional["usersuser"] = None
	type: Optional["groupsownerxtrbaninfotype"] = None


class GroupsOwnerXtrBanInfoType(enum.Enum):
	"""VK Object GroupsOwnerXtrBanInfoType

	"""
	GROUP = "group"
	PROFILE = "profile"


class GroupsProfileItem(BaseModel):
	"""VK Object GroupsProfileItem

	id - User id
	photo_50 - Url for user photo
	photo_100 - Url for user photo
	first_name - User first name
	"""
	id: Optional["integer"] = None
	photo_50: Optional["string"] = None
	photo_100: Optional["string"] = None
	first_name: Optional["string"] = None


class GroupsRoleOptions(enum.Enum):
	"""VK Object GroupsRoleOptions

	"""
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	CREATOR = "creator"


class GroupsSettingsTwitter(BaseModel):
	"""VK Object GroupsSettingsTwitter

	"""
	status: Optional["string"] = None
	name: Optional["string"] = None


class GroupsSubjectItem(BaseModel):
	"""VK Object GroupsSubjectItem

	id - Subject ID
	name - Subject title
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class GroupsTokenPermissionSetting(BaseModel):
	"""VK Object GroupsTokenPermissionSetting

	"""
	name: Optional["string"] = None
	setting: Optional["integer"] = None


class GroupsUserXtrRole(UsersUserFull):
	"""VK Object GroupsUserXtrRole

	"""
	role = None


class LikesType(enum.Enum):
	"""VK Object LikesType

	"""
	POST = "post"
	COMMENT = "comment"
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	NOTE = "note"
	MARKET = "market"
	PHOTO_COMMENT = "photo_comment"
	VIDEO_COMMENT = "video_comment"
	TOPIC_COMMENT = "topic_comment"
	MARKET_COMMENT = "market_comment"
	SITEPAGE = "sitepage"


class LinkTargetObject(BaseModel):
	"""VK Object LinkTargetObject

	type - Object type
	owner_id - Owner ID
	item_id - Item ID
	"""
	type: Optional["string"] = None
	owner_id: Optional["integer"] = None
	item_id: Optional["integer"] = None


class MarketCurrency(BaseModel):
	"""VK Object MarketCurrency

	id - Currency ID
	name - Currency sign
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class MarketMarketAlbum(BaseModel):
	"""VK Object MarketMarketAlbum

	count - Items number
	id - Market album ID
	owner_id - Market album owner's ID
	photo - 
	title - Market album title
	updated_time - Date when album has been updated last time in Unixtime
	"""
	count: Optional["integer"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	photo: Optional["photosphoto"] = None
	title: Optional["string"] = None
	updated_time: Optional["integer"] = None


class MarketMarketCategory(BaseModel):
	"""VK Object MarketMarketCategory

	"""


class MarketMarketCategoryNested(BaseModel):
	"""VK Object MarketMarketCategoryNested

	id - Category ID
	name - Category name
	parent - 
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	parent: Optional["marketmarketcategorynested"] = None


class MarketMarketCategoryOld(BaseModel):
	"""VK Object MarketMarketCategoryOld

	id - Category ID
	name - Category name
	section - 
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	section: Optional["marketsection"] = None


class MarketMarketCategoryTree(BaseModel):
	"""VK Object MarketMarketCategoryTree

	id - Category ID
	name - Category name
	children - 
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	children: Optional["marketmarketcategorytree"] = None


class MarketMarketItem(BaseModel):
	"""VK Object MarketMarketItem

	access_key - Access key for the market item
	availability - 
	button_title - Title for button for url
	category - 
	date - Date when the item has been created in Unixtime
	description - Item description
	external_id - 
	id - Item ID
	is_favorite - 
	owner_id - Item owner's ID
	price - 
	thumb_photo - URL of the preview image
	title - Item title
	url - URL to item
	variants_grouping_id - 
	is_main_variant - 
	"""
	access_key: Optional["string"] = None
	availability: Optional["marketmarketitemavailability"] = None
	button_title: Optional["string"] = None
	category: Optional["marketmarketcategory"] = None
	date: Optional["integer"] = None
	description: Optional["string"] = None
	external_id: Optional["string"] = None
	id: Optional["integer"] = None
	is_favorite: Optional["boolean"] = None
	owner_id: Optional["integer"] = None
	price: Optional["marketprice"] = None
	thumb_photo: Optional["string"] = None
	title: Optional["string"] = None
	url: Optional["string"] = None
	variants_grouping_id: Optional["integer"] = None
	is_main_variant: Optional["boolean"] = None


class MarketMarketItemAvailability(enum.IntEnum):
	"""VK Object MarketMarketItemAvailability

	"""
	available = 0
	removed = 1
	unavailable = 2


class MarketMarketItemFull(MarketMarketItem):
	"""VK Object MarketMarketItemFull

	albums_ids - 
	photos - 
	can_comment - Information whether current use can comment the item
	can_repost - Information whether current use can repost the item
	likes - 
	reposts - 
	views_count - Views number
	wishlist_item_id - Object identifier in wishlist of viewer
	cancel_info - Information for cancel and revert order
	user_agreement_info - User agreement info
	"""
	albums_ids = None
	photos = None
	can_comment = None
	can_repost = None
	likes = None
	reposts = None
	views_count = None
	wishlist_item_id = None
	cancel_info = None
	user_agreement_info = None


class MarketOrder(BaseModel):
	"""VK Object MarketOrder

	id - 
	group_id - 
	user_id - 
	display_order_id - 
	date - 
	status - 
	items_count - 
	track_number - 
	track_link - 
	comment - 
	address - 
	merchant_comment - 
	weight - 
	total_price - 
	preview_order_items - Several order items for preview
	cancel_info - Information for cancel and revert order
	"""
	id: Optional["integer"] = None
	group_id: Optional["integer"] = None
	user_id: Optional["integer"] = None
	display_order_id: Optional["string"] = None
	date: Optional["integer"] = None
	status: Optional["integer"] = None
	items_count: Optional["integer"] = None
	track_number: Optional["string"] = None
	track_link: Optional["string"] = None
	comment: Optional["string"] = None
	address: Optional["string"] = None
	merchant_comment: Optional["string"] = None
	weight: Optional["integer"] = None
	total_price: Optional["marketprice"] = None
	preview_order_items: Optional["marketorderitem"] = None
	cancel_info: Optional["baselink"] = None


class MarketOrderItem(BaseModel):
	"""VK Object MarketOrderItem

	"""
	owner_id: Optional["integer"] = None
	item_id: Optional["integer"] = None
	price: Optional["marketprice"] = None
	quantity: Optional["integer"] = None
	item: Optional["marketmarketitem"] = None
	title: Optional["string"] = None
	photo: Optional["photosphoto"] = None
	variants: Optional["string"] = None


class MarketPrice(BaseModel):
	"""VK Object MarketPrice

	amount - Amount
	currency - 
	discount_rate - 
	old_amount - 
	text - Text
	old_amount_text - Textual representation of old price
	"""
	amount: Optional["string"] = None
	currency: Optional["marketcurrency"] = None
	discount_rate: Optional["integer"] = None
	old_amount: Optional["string"] = None
	text: Optional["string"] = None
	old_amount_text: Optional["string"] = None


class MarketSection(BaseModel):
	"""VK Object MarketSection

	id - Section ID
	name - Section name
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None


class MediaRestriction(BaseModel):
	"""VK Object MediaRestriction

	text - 
	title - 
	button - 
	always_shown - Need show restriction always or not
	blur - Need blur current video or not
	can_play - Can play video or not
	can_preview - Can preview video or not
	card_icon - 
	list_icon - 
	"""
	text: Optional["string"] = None
	title: Optional["string"] = None
	button: Optional["videorestrictionbutton"] = None
	always_shown: Optional["baseboolint"] = None
	blur: Optional["baseboolint"] = None
	can_play: Optional["baseboolint"] = None
	can_preview: Optional["baseboolint"] = None
	card_icon: Optional["baseimage"] = None
	list_icon: Optional["baseimage"] = None


class MessagesAudioMessage(BaseModel):
	"""VK Object MessagesAudioMessage

	access_key - Access key for audio message
	transcript_error - 
	duration - Audio message duration in seconds
	id - Audio message ID
	link_mp3 - MP3 file URL
	link_ogg - OGG file URL
	owner_id - Audio message owner ID
	waveform - 
	"""
	access_key: Optional["string"] = None
	transcript_error: Optional["integer"] = None
	duration: Optional["integer"] = None
	id: Optional["integer"] = None
	link_mp3: Optional["string"] = None
	link_ogg: Optional["string"] = None
	owner_id: Optional["integer"] = None
	waveform: Optional["integer"] = None


class MessagesChat(BaseModel):
	"""VK Object MessagesChat

	admin_id - Chat creator ID
	id - Chat ID
	kicked - Shows that user has been kicked from the chat
	left - Shows that user has been left the chat
	photo_100 - URL of the preview image with 100 px in width
	photo_200 - URL of the preview image with 200 px in width
	photo_50 - URL of the preview image with 50 px in width
	push_settings - 
	title - Chat title
	type - Chat type
	users - 
	is_default_photo - If provided photo is default
	"""
	admin_id: Optional["integer"] = None
	id: Optional["integer"] = None
	kicked: Optional["baseboolint"] = None
	left: Optional["baseboolint"] = None
	photo_100: Optional["string"] = None
	photo_200: Optional["string"] = None
	photo_50: Optional["string"] = None
	push_settings: Optional["messageschatpushsettings"] = None
	title: Optional["string"] = None
	type: Optional["string"] = None
	users: Optional["integer"] = None
	is_default_photo: Optional["boolean"] = None


class MessagesChatFull(BaseModel):
	"""VK Object MessagesChatFull

	admin_id - Chat creator ID
	id - Chat ID
	kicked - Shows that user has been kicked from the chat
	left - Shows that user has been left the chat
	photo_100 - URL of the preview image with 100 px in width
	photo_200 - URL of the preview image with 200 px in width
	photo_50 - URL of the preview image with 50 px in width
	push_settings - 
	title - Chat title
	type - Chat type
	users - 
	"""
	admin_id: Optional["integer"] = None
	id: Optional["integer"] = None
	kicked: Optional["baseboolint"] = None
	left: Optional["baseboolint"] = None
	photo_100: Optional["string"] = None
	photo_200: Optional["string"] = None
	photo_50: Optional["string"] = None
	push_settings: Optional["messageschatpushsettings"] = None
	title: Optional["string"] = None
	type: Optional["string"] = None
	users: Optional["messagesuserxtrinvitedby"] = None


class MessagesChatPreview(BaseModel):
	"""VK Object MessagesChatPreview

	"""
	admin_id: Optional["integer"] = None
	joined: Optional["boolean"] = None
	local_id: Optional["integer"] = None
	members: Optional["integer"] = None
	members_count: Optional["integer"] = None
	title: Optional["string"] = None
	is_member: Optional["boolean"] = None


class MessagesChatPushSettings(BaseModel):
	"""VK Object MessagesChatPushSettings

	disabled_until - Time until that notifications are disabled
	sound - Information whether the sound is on
	"""
	disabled_until: Optional["integer"] = None
	sound: Optional["baseboolint"] = None


class MessagesChatRestrictions(BaseModel):
	"""VK Object MessagesChatRestrictions

	admins_promote_users - Only admins can promote users to admins
	only_admins_edit_info - Only admins can change chat info
	only_admins_edit_pin - Only admins can edit pinned message
	only_admins_invite - Only admins can invite users to this chat
	only_admins_kick - Only admins can kick users from this chat
	"""
	admins_promote_users: Optional["boolean"] = None
	only_admins_edit_info: Optional["boolean"] = None
	only_admins_edit_pin: Optional["boolean"] = None
	only_admins_invite: Optional["boolean"] = None
	only_admins_kick: Optional["boolean"] = None


class MessagesChatSettings(BaseModel):
	"""VK Object MessagesChatSettings

	members_count - 
	friends_count - 
	owner_id - 
	title - Chat title
	pinned_message - 
	state - 
	photo - 
	admin_ids - Ids of chat admins
	active_ids - 
	is_group_channel - 
	acl - 
	permissions - 
	is_disappearing - 
	theme - 
	disappearing_chat_link - 
	is_service - 
	"""
	members_count: Optional["integer"] = None
	friends_count: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	title: Optional["string"] = None
	pinned_message: Optional["messagespinnedmessage"] = None
	state: Optional["messageschatsettingsstate"] = None
	photo: Optional["messageschatsettingsphoto"] = None
	admin_ids: Optional["integer"] = None
	active_ids: Optional["integer"] = None
	is_group_channel: Optional["boolean"] = None
	acl: Optional["messageschatsettingsacl"] = None
	permissions: Optional["messageschatsettingspermissions"] = None
	is_disappearing: Optional["boolean"] = None
	theme: Optional["string"] = None
	disappearing_chat_link: Optional["string"] = None
	is_service: Optional["boolean"] = None


class MessagesChatSettingsAcl(BaseModel):
	"""VK Object MessagesChatSettingsAcl

	can_change_info - Can you change photo, description and name
	can_change_invite_link - Can you change invite link for this chat
	can_change_pin - Can you pin/unpin message for this chat
	can_invite - Can you invite other peers in chat
	can_promote_users - Can you promote simple users to chat admins
	can_see_invite_link - Can you see invite link for this chat
	can_moderate - Can you moderate (delete) other users' messages
	can_copy_chat - Can you copy chat
	can_call - Can you init group call in the chat
	can_use_mass_mentions - Can you use mass mentions
	can_change_service_type - Can you change chat service type
	"""
	can_change_info: Optional["boolean"] = None
	can_change_invite_link: Optional["boolean"] = None
	can_change_pin: Optional["boolean"] = None
	can_invite: Optional["boolean"] = None
	can_promote_users: Optional["boolean"] = None
	can_see_invite_link: Optional["boolean"] = None
	can_moderate: Optional["boolean"] = None
	can_copy_chat: Optional["boolean"] = None
	can_call: Optional["boolean"] = None
	can_use_mass_mentions: Optional["boolean"] = None
	can_change_service_type: Optional["boolean"] = None


class MessagesChatSettingsPermissions(BaseModel):
	"""VK Object MessagesChatSettingsPermissions

	invite - Who can invite users to chat
	change_info - Who can change chat info
	change_pin - Who can change pinned message
	use_mass_mentions - Who can use mass mentions
	see_invite_link - Who can see invite link
	call - Who can make calls
	change_admins - Who can change admins
	"""
	invite: Optional["string"] = None
	change_info: Optional["string"] = None
	change_pin: Optional["string"] = None
	use_mass_mentions: Optional["string"] = None
	see_invite_link: Optional["string"] = None
	call: Optional["string"] = None
	change_admins: Optional["string"] = None


class MessagesChatSettingsPhoto(BaseModel):
	"""VK Object MessagesChatSettingsPhoto

	photo_50 - URL of the preview image with 50px in width
	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	is_default_photo - If provided photo is default
	"""
	photo_50: Optional["string"] = None
	photo_100: Optional["string"] = None
	photo_200: Optional["string"] = None
	is_default_photo: Optional["boolean"] = None


class MessagesChatSettingsState(enum.Enum):
	"""VK Object MessagesChatSettingsState

	"""
	IN = "in"
	KICKED = "kicked"
	LEFT = "left"


class MessagesConversation(BaseModel):
	"""VK Object MessagesConversation

	peer - 
	sort_id - 
	last_message_id - ID of the last message in conversation
	in_read - Last message user have read
	out_read - Last outcoming message have been read by the opponent
	unread_count - Unread messages number
	is_marked_unread - Is this conversation uread
	out_read_by - 
	important - 
	unanswered - 
	special_service_type - 
	message_request_data - 
	mentions - Ids of messages with mentions
	current_keyboard - 
	push_settings - 
	can_write - 
	chat_settings - 
	"""
	peer: Optional["messagesconversationpeer"] = None
	sort_id: Optional["messagesconversationsortid"] = None
	last_message_id: Optional["integer"] = None
	in_read: Optional["integer"] = None
	out_read: Optional["integer"] = None
	unread_count: Optional["integer"] = None
	is_marked_unread: Optional["boolean"] = None
	out_read_by: Optional["messagesoutreadby"] = None
	important: Optional["boolean"] = None
	unanswered: Optional["boolean"] = None
	special_service_type: Optional["string"] = None
	message_request_data: Optional["messagesmessagerequestdata"] = None
	mentions: Optional["integer"] = None
	current_keyboard: Optional["messageskeyboard"] = None
	push_settings: Optional["messagespushsettings"] = None
	can_write: Optional["messagesconversationcanwrite"] = None
	chat_settings: Optional["messageschatsettings"] = None


class MessagesConversationCanWrite(BaseModel):
	"""VK Object MessagesConversationCanWrite

	"""
	allowed: Optional["boolean"] = None
	reason: Optional["integer"] = None


class MessagesConversationMember(BaseModel):
	"""VK Object MessagesConversationMember

	can_kick - Is it possible for user to kick this member
	invited_by - 
	is_admin - 
	is_owner - 
	is_message_request - 
	join_date - 
	request_date - Message request date
	member_id - 
	"""
	can_kick: Optional["boolean"] = None
	invited_by: Optional["integer"] = None
	is_admin: Optional["boolean"] = None
	is_owner: Optional["boolean"] = None
	is_message_request: Optional["boolean"] = None
	join_date: Optional["integer"] = None
	request_date: Optional["integer"] = None
	member_id: Optional["integer"] = None


class MessagesConversationPeer(BaseModel):
	"""VK Object MessagesConversationPeer

	"""
	id: Optional["integer"] = None
	local_id: Optional["integer"] = None
	type: Optional["messagesconversationpeertype"] = None


class MessagesConversationPeerType(enum.Enum):
	"""VK Object MessagesConversationPeerType

	"""
	CHAT = "chat"
	EMAIL = "email"
	USER = "user"
	GROUP = "group"


class MessagesConversationSortId(BaseModel):
	"""VK Object MessagesConversationSortId

	major_id - Major id for sorting conversations
	minor_id - Minor id for sorting conversations
	"""
	major_id: Optional["integer"] = None
	minor_id: Optional["integer"] = None


class MessagesConversationWithMessage(BaseModel):
	"""VK Object MessagesConversationWithMessage

	"""
	conversation: Optional["messagesconversation"] = None
	last_message: Optional["messagesmessage"] = None


class MessagesForeignMessage(BaseModel):
	"""VK Object MessagesForeignMessage

	attachments - 
	conversation_message_id - Conversation message ID
	date - Date when the message was created
	from_id - Message author's ID
	fwd_messages - 
	geo - 
	id - Message ID
	peer_id - Peer ID
	reply_message - 
	text - Message text
	update_time - Date when the message has been updated in Unixtime
	was_listened - Was the audio message inside already listened by you
	payload - Additional data sent along with message for developer convenience
	"""
	attachments: Optional["messagesmessageattachment"] = None
	conversation_message_id: Optional["integer"] = None
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	fwd_messages: Optional["messagesforeignmessage"] = None
	geo: Optional["basegeo"] = None
	id: Optional["integer"] = None
	peer_id: Optional["integer"] = None
	reply_message: Optional["messagesforeignmessage"] = None
	text: Optional["string"] = None
	update_time: Optional["integer"] = None
	was_listened: Optional["boolean"] = None
	payload: Optional["string"] = None


class MessagesForward(BaseModel):
	"""VK Object MessagesForward

	owner_id - Messages owner_id
	peer_id - Messages peer_id
	conversation_message_ids - 
	message_ids - 
	is_reply - If you need to reply to a message
	"""
	owner_id: Optional["integer"] = None
	peer_id: Optional["integer"] = None
	conversation_message_ids: Optional["integer"] = None
	message_ids: Optional["integer"] = None
	is_reply: Optional["boolean"] = None


class MessagesGraffiti(BaseModel):
	"""VK Object MessagesGraffiti

	access_key - Access key for graffiti
	height - Graffiti height
	id - Graffiti ID
	owner_id - Graffiti owner ID
	url - Graffiti URL
	width - Graffiti width
	"""
	access_key: Optional["string"] = None
	height: Optional["integer"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	url: Optional["string"] = None
	width: Optional["integer"] = None


class MessagesHistoryAttachment(BaseModel):
	"""VK Object MessagesHistoryAttachment

	attachment - 
	message_id - Message ID
	from_id - Message author's ID
	forward_level - Forward level (optional)
	"""
	attachment: Optional["messageshistorymessageattachment"] = None
	message_id: Optional["integer"] = None
	from_id: Optional["integer"] = None
	forward_level: Optional["integer"] = None


class MessagesHistoryMessageAttachment(BaseModel):
	"""VK Object MessagesHistoryMessageAttachment

	"""
	audio: Optional["audioaudio"] = None
	audio_message: Optional["messagesaudiomessage"] = None
	doc: Optional["docsdoc"] = None
	graffiti: Optional["messagesgraffiti"] = None
	link: Optional["baselink"] = None
	market: Optional["baselink"] = None
	photo: Optional["photosphoto"] = None
	share: Optional["baselink"] = None
	type: Optional["messageshistorymessageattachmenttype"] = None
	video: Optional["videovideo"] = None
	wall: Optional["baselink"] = None


class MessagesHistoryMessageAttachmentType(enum.Enum):
	"""VK Object MessagesHistoryMessageAttachmentType

	"""
	PHOTO = "photo"
	VIDEO = "video"
	AUDIO = "audio"
	DOC = "doc"
	LINK = "link"
	MARKET = "market"
	WALL = "wall"
	SHARE = "share"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(BaseModel):
	"""VK Object MessagesKeyboard

	author_id - Community or bot, which set this keyboard
	buttons - 
	one_time - Should this keyboard disappear on first use
	inline - 
	"""
	author_id: Optional["integer"] = None
	buttons: Optional["array"] = None
	one_time: Optional["boolean"] = None
	inline: Optional["boolean"] = None


class MessagesKeyboardButton(BaseModel):
	"""VK Object MessagesKeyboardButton

	action - 
	color - Button color
	"""
	action: Optional["messageskeyboardbuttonaction"] = None
	color: Optional["string"] = None


class MessagesKeyboardButtonAction(BaseModel):
	"""VK Object MessagesKeyboardButtonAction

	app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
	hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
	label - Label for button
	link - link for button
	owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
	payload - Additional data sent along with message for developer convenience
	type - Button type
	"""
	app_id: Optional["integer"] = None
	hash: Optional["string"] = None
	label: Optional["string"] = None
	link: Optional["string"] = None
	owner_id: Optional["integer"] = None
	payload: Optional["string"] = None
	type: Optional["messagestemplateactiontypenames"] = None


class MessagesLastActivity(BaseModel):
	"""VK Object MessagesLastActivity

	online - Information whether user is online
	time - Time when user was online in Unixtime
	"""
	online: Optional["baseboolint"] = None
	time: Optional["integer"] = None


class MessagesLongpollMessages(BaseModel):
	"""VK Object MessagesLongpollMessages

	count - Total number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["messagesmessage"] = None


class MessagesLongpollParams(BaseModel):
	"""VK Object MessagesLongpollParams

	server - Server URL
	key - Key
	ts - Timestamp
	pts - Persistent timestamp
	"""
	server: Optional["string"] = None
	key: Optional["string"] = None
	ts: Optional["integer"] = None
	pts: Optional["integer"] = None


class MessagesMessage(BaseModel):
	"""VK Object MessagesMessage

	action - 
	admin_author_id - Only for messages from community. Contains user ID of community admin, who sent this message.
	attachments - 
	conversation_message_id - Unique auto-incremented number for all messages with this peer
	date - Date when the message has been sent in Unixtime
	deleted - Is it an deleted message
	from_id - Message author's ID
	fwd_messages - Forwarded messages
	geo - 
	id - Message ID
	important - Is it an important message
	is_hidden - 
	is_cropped - this message is cropped for bot
	keyboard - 
	members_count - Members number
	out - Information whether the message is outcoming
	payload - 
	peer_id - Peer ID
	random_id - ID used for sending messages. It returned only for outgoing messages
	ref - 
	ref_source - 
	reply_message - 
	text - Message text
	update_time - Date when the message has been updated in Unixtime
	was_listened - Was the audio message inside already listened by you
	pinned_at - Date when the message has been pinned in Unixtime
	"""
	action: Optional["messagesmessageaction"] = None
	admin_author_id: Optional["integer"] = None
	attachments: Optional["messagesmessageattachment"] = None
	conversation_message_id: Optional["integer"] = None
	date: Optional["integer"] = None
	deleted: Optional["baseboolint"] = None
	from_id: Optional["integer"] = None
	fwd_messages: Optional["messagesforeignmessage"] = None
	geo: Optional["basegeo"] = None
	id: Optional["integer"] = None
	important: Optional["boolean"] = None
	is_hidden: Optional["boolean"] = None
	is_cropped: Optional["boolean"] = None
	keyboard: Optional["messageskeyboard"] = None
	members_count: Optional["integer"] = None
	out: Optional["baseboolint"] = None
	payload: Optional["string"] = None
	peer_id: Optional["integer"] = None
	random_id: Optional["integer"] = None
	ref: Optional["string"] = None
	ref_source: Optional["string"] = None
	reply_message: Optional["messagesforeignmessage"] = None
	text: Optional["string"] = None
	update_time: Optional["integer"] = None
	was_listened: Optional["boolean"] = None
	pinned_at: Optional["integer"] = None


class MessagesMessageAction(BaseModel):
	"""VK Object MessagesMessageAction

	conversation_message_id - Message ID
	email - Email address for chat_invite_user or chat_kick_user actions
	member_id - User or email peer ID
	message - Message body of related message
	photo - 
	text - New chat title for chat_create and chat_title_update actions
	type - 
	"""
	conversation_message_id: Optional["integer"] = None
	email: Optional["string"] = None
	member_id: Optional["integer"] = None
	message: Optional["string"] = None
	photo: Optional["messagesmessageactionphoto"] = None
	text: Optional["string"] = None
	type: Optional["messagesmessageactionstatus"] = None


class MessagesMessageActionPhoto(BaseModel):
	"""VK Object MessagesMessageActionPhoto

	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	photo_50 - URL of the preview image with 50px in width
	"""
	photo_100: Optional["string"] = None
	photo_200: Optional["string"] = None
	photo_50: Optional["string"] = None


class MessagesMessageActionStatus(enum.Enum):
	"""VK Object MessagesMessageActionStatus

	"""
	CHAT_PHOTO_UPDATE = "chat_photo_update"
	CHAT_PHOTO_REMOVE = "chat_photo_remove"
	CHAT_CREATE = "chat_create"
	CHAT_TITLE_UPDATE = "chat_title_update"
	CHAT_INVITE_USER = "chat_invite_user"
	CHAT_KICK_USER = "chat_kick_user"
	CHAT_PIN_MESSAGE = "chat_pin_message"
	CHAT_UNPIN_MESSAGE = "chat_unpin_message"
	CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"


class MessagesMessageAttachment(BaseModel):
	"""VK Object MessagesMessageAttachment

	"""
	audio: Optional["audioaudio"] = None
	audio_message: Optional["messagesaudiomessage"] = None
	call: Optional["callscall"] = None
	doc: Optional["docsdoc"] = None
	gift: Optional["giftslayout"] = None
	graffiti: Optional["messagesgraffiti"] = None
	link: Optional["baselink"] = None
	market: Optional["marketmarketitem"] = None
	market_market_album: Optional["marketmarketalbum"] = None
	photo: Optional["photosphoto"] = None
	sticker: Optional["basesticker"] = None
	story: Optional["storiesstory"] = None
	type: Optional["messagesmessageattachmenttype"] = None
	video: Optional["videovideo"] = None
	wall: Optional["wallwallpostfull"] = None
	wall_reply: Optional["wallwallcomment"] = None
	poll: Optional["pollspoll"] = None


class MessagesMessageAttachmentType(enum.Enum):
	"""VK Object MessagesMessageAttachmentType

	"""
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	MARKET = "market"
	MARKET_ALBUM = "market_album"
	GIFT = "gift"
	STICKER = "sticker"
	WALL = "wall"
	WALL_REPLY = "wall_reply"
	ARTICLE = "article"
	POLL = "poll"
	CALL = "call"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(BaseModel):
	"""VK Object MessagesMessageRequestData

	status - Status of message request
	inviter_id - Message request sender id
	request_date - Message request date
	"""
	status: Optional["string"] = None
	inviter_id: Optional["integer"] = None
	request_date: Optional["integer"] = None


class MessagesMessagesArray(BaseModel):
	"""VK Object MessagesMessagesArray

	"""
	count: Optional["integer"] = None
	items: Optional["messagesmessage"] = None


class MessagesOutReadBy(BaseModel):
	"""VK Object MessagesOutReadBy

	"""
	count: Optional["integer"] = None
	member_ids: Optional["integer"] = None


class MessagesPinnedMessage(BaseModel):
	"""VK Object MessagesPinnedMessage

	attachments - 
	conversation_message_id - Unique auto-incremented number for all messages with this peer
	date - Date when the message has been sent in Unixtime
	from_id - Message author's ID
	fwd_messages - Forwarded messages
	geo - 
	id - Message ID
	peer_id - Peer ID
	reply_message - 
	text - Message text
	keyboard - 
	"""
	attachments: Optional["messagesmessageattachment"] = None
	conversation_message_id: Optional["integer"] = None
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	fwd_messages: Optional["messagesforeignmessage"] = None
	geo: Optional["basegeo"] = None
	id: Optional["integer"] = None
	peer_id: Optional["integer"] = None
	reply_message: Optional["messagesforeignmessage"] = None
	text: Optional["string"] = None
	keyboard: Optional["messageskeyboard"] = None


class MessagesPushSettings(BaseModel):
	"""VK Object MessagesPushSettings

	disabled_forever - Information whether push notifications are disabled forever
	disabled_until - Time until what notifications are disabled
	no_sound - Information whether the sound is on
	"""
	disabled_forever: Optional["boolean"] = None
	disabled_until: Optional["integer"] = None
	no_sound: Optional["boolean"] = None


class MessagesTemplateActionTypeNames(enum.Enum):
	"""VK Object MessagesTemplateActionTypeNames

	"""
	TEXT = "text"
	START = "start"
	LOCATION = "location"
	VKPAY = "vkpay"
	OPEN_APP = "open_app"
	OPEN_PHOTO = "open_photo"
	OPEN_LINK = "open_link"
	CALLBACK = "callback"


class MessagesUserXtrInvitedBy(UsersUserXtrType):
	"""VK Object MessagesUserXtrInvitedBy

	invited_by - ID of the inviter
	"""
	invited_by = None


class NewsfeedCommentsFilters(enum.Enum):
	"""VK Object NewsfeedCommentsFilters

	"""
	POST = "post"
	PHOTO = "photo"
	VIDEO = "video"
	TOPIC = "topic"
	NOTE = "note"


class NewsfeedEventActivity(BaseModel):
	"""VK Object NewsfeedEventActivity

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address: Optional["string"] = None
	button_text: Optional["string"] = None
	friends: Optional["integer"] = None
	member_status: Optional["groupsgroupfullmemberstatus"] = None
	text: Optional["string"] = None
	time: Optional["integer"] = None


class NewsfeedFilters(enum.Enum):
	"""VK Object NewsfeedFilters

	"""
	POST = "post"
	PHOTO = "photo"
	PHOTO_TAG = "photo_tag"
	WALL_PHOTO = "wall_photo"
	FRIEND = "friend"
	NOTE = "note"
	AUDIO = "audio"
	VIDEO = "video"
	AUDIO_PLAYLIST = "audio_playlist"
	CLIP = "clip"


class NewsfeedIgnoreItemType(enum.Enum):
	"""VK Object NewsfeedIgnoreItemType

	"""
	WALL = "wall"
	TAG = "tag"
	PROFILEPHOTO = "profilephoto"
	VIDEO = "video"
	PHOTO = "photo"
	AUDIO = "audio"


class NewsfeedItemAudio(NewsfeedItemBase):
	"""VK Object NewsfeedItemAudio

	audio - 
	post_id - Post ID
	"""
	audio = None
	post_id = None


class NewsfeedItemAudioAudio(BaseModel):
	"""VK Object NewsfeedItemAudioAudio

	count - Audios number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["audioaudio"] = None


class NewsfeedItemBase(BaseModel):
	"""VK Object NewsfeedItemBase

	type - 
	source_id - Item source ID
	date - Date when item has been added in Unixtime
	"""
	type: Optional["newsfeednewsfeeditemtype"] = None
	source_id: Optional["integer"] = None
	date: Optional["integer"] = None


class NewsfeedItemDigest(NewsfeedItemBase):
	"""VK Object NewsfeedItemDigest

	feed_id - id of feed in digest
	items - 
	main_post_ids - 
	template - type of digest
	header - 
	footer - 
	track_code - 
	"""
	feed_id = None
	items = None
	main_post_ids = None
	template = None
	header = None
	footer = None
	track_code = None


class NewsfeedItemDigestButton(BaseModel):
	"""VK Object NewsfeedItemDigestButton

	"""
	title: Optional["string"] = None
	style: Optional["string"] = None


class NewsfeedItemDigestFooter(BaseModel):
	"""VK Object NewsfeedItemDigestFooter

	style - 
	text - text for invite to enable smart feed
	button - 
	"""
	style: Optional["string"] = None
	text: Optional["string"] = None
	button: Optional["newsfeeditemdigestbutton"] = None


class NewsfeedItemDigestFullItem(BaseModel):
	"""VK Object NewsfeedItemDigestFullItem

	"""
	text: Optional["string"] = None
	source_name: Optional["string"] = None
	attachment_index: Optional["integer"] = None
	attachment: Optional["wallwallpostattachment"] = None
	style: Optional["string"] = None
	post: Optional["wallwallpost"] = None


class NewsfeedItemDigestHeader(BaseModel):
	"""VK Object NewsfeedItemDigestHeader

	title - Title of the header
	subtitle - Subtitle of the header, when title have two strings
	style - 
	button - 
	"""
	title: Optional["string"] = None
	subtitle: Optional["string"] = None
	style: Optional["string"] = None
	button: Optional["newsfeeditemdigestbutton"] = None


class NewsfeedItemDigestItem(BaseModel):
	"""VK Object NewsfeedItemDigestItem

	"""


class NewsfeedItemFriend(NewsfeedItemBase):
	"""VK Object NewsfeedItemFriend

	"""
	friends = None


class NewsfeedItemFriendFriends(BaseModel):
	"""VK Object NewsfeedItemFriendFriends

	count - Number of friends has been added
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["baseuserid"] = None


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
	"""VK Object NewsfeedItemHolidayRecommendationsBlockHeader

	title - Title of the header
	subtitle - Subtitle of the header
	image - 
	action - 
	"""
	title: Optional["string"] = None
	subtitle: Optional["string"] = None
	image: Optional["baseimage"] = None
	action: Optional["baselinkbuttonaction"] = None


class NewsfeedItemPhoto(WallCarouselBase,
	NewsfeedItemBase):
	"""VK Object NewsfeedItemPhoto

	photos - 
	post_id - Post ID
	"""
	photos = None
	post_id = None


class NewsfeedItemPhotoPhotos(BaseModel):
	"""VK Object NewsfeedItemPhotoPhotos

	count - Photos number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["newsfeednewsfeedphoto"] = None


class NewsfeedItemPhotoTag(WallCarouselBase,
	NewsfeedItemBase):
	"""VK Object NewsfeedItemPhotoTag

	photo_tags - 
	post_id - Post ID
	"""
	photo_tags = None
	post_id = None


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
	"""VK Object NewsfeedItemPhotoTagPhotoTags

	count - Tags number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["newsfeednewsfeedphoto"] = None


class NewsfeedItemPromoButton(NewsfeedItemBase):
	"""VK Object NewsfeedItemPromoButton

	"""
	text = None
	title = None
	action = None
	images = None
	track_code = None


class NewsfeedItemPromoButtonAction(BaseModel):
	"""VK Object NewsfeedItemPromoButtonAction

	"""
	url: Optional["string"] = None
	type: Optional["string"] = None
	target: Optional["string"] = None


class NewsfeedItemPromoButtonImage(BaseModel):
	"""VK Object NewsfeedItemPromoButtonImage

	"""
	width: Optional["integer"] = None
	height: Optional["integer"] = None
	url: Optional["string"] = None


class NewsfeedItemTopic(NewsfeedItemBase):
	"""VK Object NewsfeedItemTopic

	comments - 
	likes - 
	post_id - Topic post ID
	text - Post text
	"""
	comments = None
	likes = None
	post_id = None
	text = None


class NewsfeedItemVideo(WallCarouselBase,
	NewsfeedItemBase):
	"""VK Object NewsfeedItemVideo

	"""
	video = None


class NewsfeedItemVideoVideo(BaseModel):
	"""VK Object NewsfeedItemVideoVideo

	count - Tags number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["videovideo"] = None


class NewsfeedItemWallpost(WallCarouselBase,
	NewsfeedItemBase):
	"""VK Object NewsfeedItemWallpost

	activity - 
	attachments - 
	comments - 
	copy_history - 
	feedback - 
	geo - 
	is_favorite - Information whether the post in favorites list
	likes - 
	marked_as_ads - Information whether the post is marked as ads
	post_id - Post ID
	post_source - 
	post_type - 
	reposts - 
	signer_id - Post signer ID
	text - Post text
	views - Count of views
	short_text_rate - Preview length control parameter
	"""
	activity = None
	attachments = None
	comments = None
	copy_history = None
	feedback = None
	geo = None
	is_favorite = None
	likes = None
	marked_as_ads = None
	post_id = None
	post_source = None
	post_type = None
	reposts = None
	signer_id = None
	text = None
	views = None
	short_text_rate = None


class NewsfeedItemWallpostFeedback(BaseModel):
	"""VK Object NewsfeedItemWallpostFeedback

	"""
	type: Optional["newsfeeditemwallpostfeedbacktype"] = None
	question: Optional["string"] = None
	answers: Optional["newsfeeditemwallpostfeedbackanswer"] = None
	stars_count: Optional["integer"] = None
	gratitude: Optional["string"] = None


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
	"""VK Object NewsfeedItemWallpostFeedbackAnswer

	"""
	title: Optional["string"] = None
	id: Optional["string"] = None


class NewsfeedItemWallpostFeedbackType(enum.Enum):
	"""VK Object NewsfeedItemWallpostFeedbackType

	"""
	BUTTONS = "buttons"
	STARS = "stars"


class NewsfeedItemWallpostType(enum.Enum):
	"""VK Object NewsfeedItemWallpostType

	"""
	POST = "post"
	COPY = "copy"
	REPLY = "reply"


class NewsfeedList(BaseModel):
	"""VK Object NewsfeedList

	id - List ID
	title - List title
	"""
	id: Optional["integer"] = None
	title: Optional["string"] = None


class NewsfeedListFull(NewsfeedList):
	"""VK Object NewsfeedListFull

	no_reposts - Information whether reposts hiding is enabled
	source_ids - 
	"""
	no_reposts = None
	source_ids = None


class NewsfeedNewsfeedItem(BaseModel):
	"""VK Object NewsfeedNewsfeedItem

	"""


class NewsfeedNewsfeedItemType(enum.Enum):
	"""VK Object NewsfeedNewsfeedItemType

	"""
	POST = "post"
	PHOTO = "photo"
	PHOTO_TAG = "photo_tag"
	WALL_PHOTO = "wall_photo"
	FRIEND = "friend"
	AUDIO = "audio"
	VIDEO = "video"
	TOPIC = "topic"
	DIGEST = "digest"
	STORIES = "stories"


class NewsfeedNewsfeedPhoto(PhotosPhoto):
	"""VK Object NewsfeedNewsfeedPhoto

	likes - 
	comments - 
	can_repost - Information whether current user can repost the photo
	"""
	likes = None
	comments = None
	can_repost = None


class NotesNote(BaseModel):
	"""VK Object NotesNote

	read_comments - 
	can_comment - Information whether current user can comment the note
	comments - Comments number
	date - Date when the note has been created in Unixtime
	id - Note ID
	owner_id - Note owner's ID
	text - Note text
	text_wiki - Note text in wiki format
	title - Note title
	view_url - URL of the page with note preview
	"""
	read_comments: Optional["integer"] = None
	can_comment: Optional["baseboolint"] = None
	comments: Optional["integer"] = None
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	text: Optional["string"] = None
	text_wiki: Optional["string"] = None
	title: Optional["string"] = None
	view_url: Optional["string"] = None


class NotesNoteComment(BaseModel):
	"""VK Object NotesNoteComment

	date - Date when the comment has beed added in Unixtime
	id - Comment ID
	message - Comment text
	nid - Note ID
	oid - Note ID
	reply_to - ID of replied comment 
	uid - Comment author's ID
	"""
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	message: Optional["string"] = None
	nid: Optional["integer"] = None
	oid: Optional["integer"] = None
	reply_to: Optional["integer"] = None
	uid: Optional["integer"] = None


class NotificationsFeedback(BaseModel):
	"""VK Object NotificationsFeedback

	attachments - 
	from_id - Reply author's ID
	geo - 
	id - Item ID
	likes - 
	text - Reply text
	to_id - Wall owner's ID
	"""
	attachments: Optional["wallwallpostattachment"] = None
	from_id: Optional["integer"] = None
	geo: Optional["basegeo"] = None
	id: Optional["integer"] = None
	likes: Optional["baselikesinfo"] = None
	text: Optional["string"] = None
	to_id: Optional["integer"] = None


class NotificationsNotification(BaseModel):
	"""VK Object NotificationsNotification

	date - Date when the event has been occurred
	feedback - 
	parent - 
	reply - 
	type - Notification type
	"""
	date: Optional["integer"] = None
	feedback: Optional["notificationsfeedback"] = None
	parent: Optional["notificationsnotificationparent"] = None
	reply: Optional["notificationsreply"] = None
	type: Optional["string"] = None


class NotificationsNotificationItem(BaseModel):
	"""VK Object NotificationsNotificationItem

	"""


class NotificationsNotificationParent(WallWallpostToId,
	PhotosPhoto,
	BoardTopic,
	VideoVideo,
	NotificationsNotificationsComment):
	"""VK Object NotificationsNotificationParent

	"""


class NotificationsNotificationsComment(BaseModel):
	"""VK Object NotificationsNotificationsComment

	date - Date when the comment has been added in Unixtime
	id - Comment ID
	owner_id - Author ID
	photo - 
	post - 
	text - Comment text
	topic - 
	video - 
	"""
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	photo: Optional["photosphoto"] = None
	post: Optional["wallwallpost"] = None
	text: Optional["string"] = None
	topic: Optional["boardtopic"] = None
	video: Optional["videovideo"] = None


class NotificationsReply(BaseModel):
	"""VK Object NotificationsReply

	date - Date when the reply has been created in Unixtime
	id - Reply ID
	text - Reply text
	"""
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	text: Optional["integer"] = None


class NotificationsSendMessageError(BaseModel):
	"""VK Object NotificationsSendMessageError

	code - Error code
	description - Error description
	"""
	code: Optional["integer"] = None
	description: Optional["string"] = None


class NotificationsSendMessageItem(BaseModel):
	"""VK Object NotificationsSendMessageItem

	user_id - User ID
	status - Notification status
	error - 
	"""
	user_id: Optional["integer"] = None
	status: Optional["boolean"] = None
	error: Optional["notificationssendmessageerror"] = None


class OauthError(BaseModel):
	"""VK Object OauthError

	error - Error type
	error_description - Error description
	redirect_uri - URI for validation
	"""
	error: Optional["string"] = None
	error_description: Optional["string"] = None
	redirect_uri: Optional["string"] = None


class OrdersAmount(BaseModel):
	"""VK Object OrdersAmount

	amounts - 
	currency - Currency name
	"""
	amounts: Optional["ordersamountitem"] = None
	currency: Optional["string"] = None


class OrdersAmountItem(BaseModel):
	"""VK Object OrdersAmountItem

	amount - Votes amount in user's currency
	description - Amount description
	votes - Votes number
	"""
	amount: Optional["integer"] = None
	description: Optional["string"] = None
	votes: Optional["string"] = None


class OrdersOrder(BaseModel):
	"""VK Object OrdersOrder

	amount - Amount
	app_order_id - App order ID
	cancel_transaction_id - Cancel transaction ID
	date - Date of creation in Unixtime
	id - Order ID
	item - Order item
	receiver_id - Receiver ID
	status - Order status
	transaction_id - Transaction ID
	user_id - User ID
	"""
	amount: Optional["integer"] = None
	app_order_id: Optional["integer"] = None
	cancel_transaction_id: Optional["integer"] = None
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	item: Optional["string"] = None
	receiver_id: Optional["integer"] = None
	status: Optional["string"] = None
	transaction_id: Optional["integer"] = None
	user_id: Optional["integer"] = None


class OrdersSubscription(BaseModel):
	"""VK Object OrdersSubscription

	cancel_reason - Cancel reason
	create_time - Date of creation in Unixtime
	id - Subscription ID
	item_id - Subscription order item
	next_bill_time - Date of next bill in Unixtime
	pending_cancel - Pending cancel state
	period - Subscription period
	period_start_time - Date of last period start in Unixtime
	price - Subscription price
	status - Subscription status
	test_mode - Is test subscription
	trial_expire_time - Date of trial expire in Unixtime
	update_time - Date of last change in Unixtime
	"""
	cancel_reason: Optional["string"] = None
	create_time: Optional["integer"] = None
	id: Optional["integer"] = None
	item_id: Optional["string"] = None
	next_bill_time: Optional["integer"] = None
	pending_cancel: Optional["boolean"] = None
	period: Optional["integer"] = None
	period_start_time: Optional["integer"] = None
	price: Optional["integer"] = None
	status: Optional["string"] = None
	test_mode: Optional["boolean"] = None
	trial_expire_time: Optional["integer"] = None
	update_time: Optional["integer"] = None


class OwnerState(BaseModel):
	"""VK Object OwnerState

	state - 
	description - wiki text to describe user state
	"""
	state: Optional["integer"] = None
	description: Optional["string"] = None


class PagesPrivacySettings(enum.IntEnum):
	"""VK Object PagesPrivacySettings

	"""
	community managers only = 0
	community members only = 1
	everyone = 2


class PagesWikipage(BaseModel):
	"""VK Object PagesWikipage

	creator_id - Page creator ID
	creator_name - Page creator name
	editor_id - Last editor ID
	editor_name - Last editor name
	group_id - Community ID
	id - Page ID
	title - Page title
	views - Views number
	who_can_edit - Edit settings of the page
	who_can_view - View settings of the page
	"""
	creator_id: Optional["integer"] = None
	creator_name: Optional["integer"] = None
	editor_id: Optional["integer"] = None
	editor_name: Optional["string"] = None
	group_id: Optional["integer"] = None
	id: Optional["integer"] = None
	title: Optional["string"] = None
	views: Optional["integer"] = None
	who_can_edit: Optional["pagesprivacysettings"] = None
	who_can_view: Optional["pagesprivacysettings"] = None


class PagesWikipageFull(BaseModel):
	"""VK Object PagesWikipageFull

	created - Date when the page has been created in Unixtime
	creator_id - Page creator ID
	current_user_can_edit - Information whether current user can edit the page
	current_user_can_edit_access - Information whether current user can edit the page access settings
	edited - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	group_id - Community ID
	html - Page content, HTML
	id - Page ID
	source - Page content, wiki
	title - Page title
	view_url - URL of the page preview
	views - Views number
	who_can_edit - Edit settings of the page
	who_can_view - View settings of the page
	"""
	created: Optional["integer"] = None
	creator_id: Optional["integer"] = None
	current_user_can_edit: Optional["baseboolint"] = None
	current_user_can_edit_access: Optional["baseboolint"] = None
	edited: Optional["integer"] = None
	editor_id: Optional["integer"] = None
	group_id: Optional["integer"] = None
	html: Optional["string"] = None
	id: Optional["integer"] = None
	source: Optional["string"] = None
	title: Optional["string"] = None
	view_url: Optional["string"] = None
	views: Optional["integer"] = None
	who_can_edit: Optional["pagesprivacysettings"] = None
	who_can_view: Optional["pagesprivacysettings"] = None


class PagesWikipageHistory(BaseModel):
	"""VK Object PagesWikipageHistory

	id - Version ID
	length - Page size in bytes
	date - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	editor_name - Last editor name
	"""
	id: Optional["integer"] = None
	length: Optional["integer"] = None
	date: Optional["integer"] = None
	editor_id: Optional["integer"] = None
	editor_name: Optional["string"] = None


class PhotosCommentXtrPid(BaseModel):
	"""VK Object PhotosCommentXtrPid

	attachments - 
	date - Date when the comment has been added in Unixtime
	from_id - Author ID
	id - Comment ID
	likes - 
	pid - Photo ID
	reply_to_comment - Replied comment ID
	reply_to_user - Replied user ID
	text - Comment text
	parents_stack - 
	thread - 
	"""
	attachments: Optional["wallcommentattachment"] = None
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	id: Optional["integer"] = None
	likes: Optional["baselikesinfo"] = None
	pid: Optional["integer"] = None
	reply_to_comment: Optional["integer"] = None
	reply_to_user: Optional["integer"] = None
	text: Optional["string"] = None
	parents_stack: Optional["integer"] = None
	thread: Optional["commentthread"] = None


class PhotosImage(BaseModel):
	"""VK Object PhotosImage

	height - Height of the photo in px.
	type - 
	url - Photo URL.
	width - Width of the photo in px.
	"""
	height: Optional["integer"] = None
	type: Optional["photosimagetype"] = None
	url: Optional["string"] = None
	width: Optional["integer"] = None


class PhotosImageType(enum.Enum):
	"""VK Object PhotosImageType

	"""
	S = "s"
	M = "m"
	X = "x"
	L = "l"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	Y = "y"
	Z = "z"
	W = "w"


class PhotosPhoto(BaseModel):
	"""VK Object PhotosPhoto

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	images - 
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_256 - URL of image with 2560 px width
	can_comment - Information whether current user can comment the photo
	place - 
	post_id - Post ID
	sizes - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	has_tags - Whether photo has attached tag links
	restrictions - 
	"""
	access_key: Optional["string"] = None
	album_id: Optional["integer"] = None
	date: Optional["integer"] = None
	height: Optional["integer"] = None
	id: Optional["integer"] = None
	images: Optional["photosimage"] = None
	lat: Optional["number"] = None
	long: Optional["number"] = None
	owner_id: Optional["integer"] = None
	photo_256: Optional["string"] = None
	can_comment: Optional["baseboolint"] = None
	place: Optional["string"] = None
	post_id: Optional["integer"] = None
	sizes: Optional["photosphotosizes"] = None
	text: Optional["string"] = None
	user_id: Optional["integer"] = None
	width: Optional["integer"] = None
	has_tags: Optional["boolean"] = None
	restrictions: Optional["mediarestriction"] = None


class PhotosPhotoAlbum(BaseModel):
	"""VK Object PhotosPhotoAlbum

	created - Date when the album has been created in Unixtime
	description - Photo album description
	id - Photo album ID
	owner_id - Album owner's ID
	size - Photos number
	thumb - 
	title - Photo album title
	updated - Date when the album has been updated last time in Unixtime
	"""
	created: Optional["integer"] = None
	description: Optional["string"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	size: Optional["integer"] = None
	thumb: Optional["photosphoto"] = None
	title: Optional["string"] = None
	updated: Optional["integer"] = None


class PhotosPhotoAlbumFull(BaseModel):
	"""VK Object PhotosPhotoAlbumFull

	can_upload - Information whether current user can upload photo to the album
	comments_disabled - Information whether album comments are disabled
	created - Date when the album has been created in Unixtime
	description - Photo album description
	id - Photo album ID
	owner_id - Album owner's ID
	size - Photos number
	sizes - 
	thumb_id - Thumb photo ID
	thumb_is_last - Information whether the album thumb is last photo
	thumb_src - URL of the thumb image
	title - Photo album title
	updated - Date when the album has been updated last time in Unixtime
	upload_by_admins_only - Information whether only community administrators can upload photos
	"""
	can_upload: Optional["baseboolint"] = None
	comments_disabled: Optional["baseboolint"] = None
	created: Optional["integer"] = None
	description: Optional["string"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	size: Optional["integer"] = None
	sizes: Optional["photosphotosizes"] = None
	thumb_id: Optional["integer"] = None
	thumb_is_last: Optional["baseboolint"] = None
	thumb_src: Optional["string"] = None
	title: Optional["string"] = None
	updated: Optional["integer"] = None
	upload_by_admins_only: Optional["baseboolint"] = None


class PhotosPhotoFalseable(BaseModel):
	"""VK Object PhotosPhotoFalseable

	"""


class PhotosPhotoFull(BaseModel):
	"""VK Object PhotosPhotoFull

	access_key - Access key for the photo
	album_id - Album ID
	can_comment - Information whether current user can comment the photo
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	images - 
	lat - Latitude
	likes - 
	reposts - 
	comments - 
	long - Longitude
	owner_id - Photo owner's ID
	post_id - Post ID
	tags - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key: Optional["string"] = None
	album_id: Optional["integer"] = None
	can_comment: Optional["baseboolint"] = None
	date: Optional["integer"] = None
	height: Optional["integer"] = None
	id: Optional["integer"] = None
	images: Optional["photosimage"] = None
	lat: Optional["number"] = None
	likes: Optional["baselikes"] = None
	reposts: Optional["baserepostsinfo"] = None
	comments: Optional["baseobjectcount"] = None
	long: Optional["number"] = None
	owner_id: Optional["integer"] = None
	post_id: Optional["integer"] = None
	tags: Optional["baseobjectcount"] = None
	text: Optional["string"] = None
	user_id: Optional["integer"] = None
	width: Optional["integer"] = None


class PhotosPhotoFullXtrRealOffset(BaseModel):
	"""VK Object PhotosPhotoFullXtrRealOffset

	access_key - Access key for the photo
	album_id - Album ID
	can_comment - 
	comments - 
	date - Date when uploaded
	height - Original photo height
	hidden - Returns if the photo is hidden above the wall
	id - Photo ID
	lat - Latitude
	likes - 
	long - Longitude
	owner_id - Photo owner's ID
	photo_1280 - URL of image with 1280 px width
	photo_130 - URL of image with 130 px width
	photo_2560 - URL of image with 2560 px width
	photo_604 - URL of image with 604 px width
	photo_75 - URL of image with 75 px width
	photo_807 - URL of image with 807 px width
	post_id - Post ID
	real_offset - Real position of the photo
	reposts - 
	sizes - 
	tags - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key: Optional["string"] = None
	album_id: Optional["integer"] = None
	can_comment: Optional["baseboolint"] = None
	comments: Optional["baseobjectcount"] = None
	date: Optional["integer"] = None
	height: Optional["integer"] = None
	hidden: Optional["basepropertyexists"] = None
	id: Optional["integer"] = None
	lat: Optional["number"] = None
	likes: Optional["baselikes"] = None
	long: Optional["number"] = None
	owner_id: Optional["integer"] = None
	photo_1280: Optional["string"] = None
	photo_130: Optional["string"] = None
	photo_2560: Optional["string"] = None
	photo_604: Optional["string"] = None
	photo_75: Optional["string"] = None
	photo_807: Optional["string"] = None
	post_id: Optional["integer"] = None
	real_offset: Optional["integer"] = None
	reposts: Optional["baseobjectcount"] = None
	sizes: Optional["photosphotosizes"] = None
	tags: Optional["baseobjectcount"] = None
	text: Optional["string"] = None
	user_id: Optional["integer"] = None
	width: Optional["integer"] = None


class PhotosPhotoSizes(BaseModel):
	"""VK Object PhotosPhotoSizes

	height - Height in px
	url - URL of the image
	src - URL of the image
	type - 
	width - Width in px
	"""
	height: Optional["integer"] = None
	url: Optional["string"] = None
	src: Optional["string"] = None
	type: Optional["photosphotosizestype"] = None
	width: Optional["integer"] = None


class PhotosPhotoSizesType(enum.Enum):
	"""VK Object PhotosPhotoSizesType

	"""
	S = "s"
	M = "m"
	X = "x"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	K = "k"
	L = "l"
	Y = "y"
	Z = "z"
	C = "c"
	W = "w"
	A = "a"
	B = "b"
	E = "e"
	I = "i"
	D = "d"
	J = "j"
	TEMP = "temp"
	H = "h"
	G = "g"
	N = "n"
	F = "f"
	MAX = "max"


class PhotosPhotoTag(BaseModel):
	"""VK Object PhotosPhotoTag

	date - Date when tag has been added in Unixtime
	id - Tag ID
	placer_id - ID of the tag creator
	tagged_name - Tag description
	description - Tagged description.
	user_id - Tagged user ID
	viewed - Information whether the tag is reviewed
	x - Coordinate X of the left upper corner
	x2 - Coordinate X of the right lower corner
	y - Coordinate Y of the left upper corner
	y2 - Coordinate Y of the right lower corner
	"""
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	placer_id: Optional["integer"] = None
	tagged_name: Optional["string"] = None
	description: Optional["string"] = None
	user_id: Optional["integer"] = None
	viewed: Optional["baseboolint"] = None
	x: Optional["number"] = None
	x2: Optional["number"] = None
	y: Optional["number"] = None
	y2: Optional["number"] = None


class PhotosPhotoUpload(BaseModel):
	"""VK Object PhotosPhotoUpload

	album_id - Album ID
	upload_url - URL to upload photo
	fallback_upload_url - Fallback URL if upload_url returned error
	user_id - User ID
	group_id - Group ID
	"""
	album_id: Optional["integer"] = None
	upload_url: Optional["string"] = None
	fallback_upload_url: Optional["string"] = None
	user_id: Optional["integer"] = None
	group_id: Optional["integer"] = None


class PhotosPhotoXtrRealOffset(BaseModel):
	"""VK Object PhotosPhotoXtrRealOffset

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	hidden - Returns if the photo is hidden above the wall
	id - Photo ID
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_1280 - URL of image with 1280 px width
	photo_130 - URL of image with 130 px width
	photo_2560 - URL of image with 2560 px width
	photo_604 - URL of image with 604 px width
	photo_75 - URL of image with 75 px width
	photo_807 - URL of image with 807 px width
	post_id - Post ID
	real_offset - Real position of the photo
	sizes - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key: Optional["string"] = None
	album_id: Optional["integer"] = None
	date: Optional["integer"] = None
	height: Optional["integer"] = None
	hidden: Optional["basepropertyexists"] = None
	id: Optional["integer"] = None
	lat: Optional["number"] = None
	long: Optional["number"] = None
	owner_id: Optional["integer"] = None
	photo_1280: Optional["string"] = None
	photo_130: Optional["string"] = None
	photo_2560: Optional["string"] = None
	photo_604: Optional["string"] = None
	photo_75: Optional["string"] = None
	photo_807: Optional["string"] = None
	post_id: Optional["integer"] = None
	real_offset: Optional["integer"] = None
	sizes: Optional["photosphotosizes"] = None
	text: Optional["string"] = None
	user_id: Optional["integer"] = None
	width: Optional["integer"] = None


class PhotosPhotoXtrTagInfo(BaseModel):
	"""VK Object PhotosPhotoXtrTagInfo

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_1280 - URL of image with 1280 px width
	photo_130 - URL of image with 130 px width
	photo_2560 - URL of image with 2560 px width
	photo_604 - URL of image with 604 px width
	photo_75 - URL of image with 75 px width
	photo_807 - URL of image with 807 px width
	placer_id - ID of the tag creator
	post_id - Post ID
	sizes - 
	tag_created - Date when tag has been added in Unixtime
	tag_id - Tag ID
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key: Optional["string"] = None
	album_id: Optional["integer"] = None
	date: Optional["integer"] = None
	height: Optional["integer"] = None
	id: Optional["integer"] = None
	lat: Optional["number"] = None
	long: Optional["number"] = None
	owner_id: Optional["integer"] = None
	photo_1280: Optional["string"] = None
	photo_130: Optional["string"] = None
	photo_2560: Optional["string"] = None
	photo_604: Optional["string"] = None
	photo_75: Optional["string"] = None
	photo_807: Optional["string"] = None
	placer_id: Optional["integer"] = None
	post_id: Optional["integer"] = None
	sizes: Optional["photosphotosizes"] = None
	tag_created: Optional["integer"] = None
	tag_id: Optional["integer"] = None
	text: Optional["string"] = None
	user_id: Optional["integer"] = None
	width: Optional["integer"] = None


class PhotosTagsSuggestionItem(BaseModel):
	"""VK Object PhotosTagsSuggestionItem

	"""
	title: Optional["string"] = None
	caption: Optional["string"] = None
	type: Optional["string"] = None
	buttons: Optional["photostagssuggestionitembutton"] = None
	photo: Optional["photosphoto"] = None
	tags: Optional["photosphototag"] = None
	track_code: Optional["string"] = None


class PhotosTagsSuggestionItemButton(BaseModel):
	"""VK Object PhotosTagsSuggestionItemButton

	"""
	title: Optional["string"] = None
	action: Optional["string"] = None
	style: Optional["string"] = None


class PodcastCover(BaseModel):
	"""VK Object PodcastCover

	"""
	sizes: Optional["photosphotosizes"] = None


class PodcastExternalData(BaseModel):
	"""VK Object PodcastExternalData

	url - Url of the podcast page
	owner_url - Url of the podcasts owner community
	title - Podcast title
	owner_name - Name of the podcasts owner community
	cover - Podcast cover
	"""
	url: Optional["string"] = None
	owner_url: Optional["string"] = None
	title: Optional["string"] = None
	owner_name: Optional["string"] = None
	cover: Optional["podcastcover"] = None


class PollsAnswer(BaseModel):
	"""VK Object PollsAnswer

	id - Answer ID
	rate - Answer rate in percents
	text - Answer text
	votes - Votes number
	"""
	id: Optional["integer"] = None
	rate: Optional["number"] = None
	text: Optional["string"] = None
	votes: Optional["integer"] = None


class PollsBackground(BaseModel):
	"""VK Object PollsBackground

	angle - Gradient angle with 0 on positive X axis
	color - Hex color code without #
	height - Original height of pattern tile
	id - 
	name - 
	images - Pattern tiles
	points - Gradient points
	type - 
	width - Original with of pattern tile
	"""
	angle: Optional["integer"] = None
	color: Optional["string"] = None
	height: Optional["integer"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None
	images: Optional["baseimage"] = None
	points: Optional["basegradientpoint"] = None
	type: Optional["string"] = None
	width: Optional["integer"] = None


class PollsFriend(BaseModel):
	"""VK Object PollsFriend

	"""
	id: Optional["integer"] = None


class PollsPoll(BaseModel):
	"""VK Object PollsPoll

	anonymous - 
	friends - 
	multiple - Information whether the poll with multiple choices
	answer_id - Current user's answer ID
	end_date - 
	answer_ids - Current user's answer IDs
	closed - 
	is_board - 
	can_edit - 
	can_vote - 
	can_report - 
	can_share - 
	photo - 
	answers - 
	created - Date when poll has been created in Unixtime
	id - Poll ID
	owner_id - Poll owner's ID
	author_id - Poll author's ID
	question - Poll question
	background - 
	votes - Votes number
	disable_unvote - 
	"""
	anonymous: Optional["pollspollanonymous"] = None
	friends: Optional["pollsfriend"] = None
	multiple: Optional["boolean"] = None
	answer_id: Optional["integer"] = None
	end_date: Optional["integer"] = None
	answer_ids: Optional["integer"] = None
	closed: Optional["boolean"] = None
	is_board: Optional["boolean"] = None
	can_edit: Optional["boolean"] = None
	can_vote: Optional["boolean"] = None
	can_report: Optional["boolean"] = None
	can_share: Optional["boolean"] = None
	photo: Optional["pollsbackground"] = None
	answers: Optional["pollsanswer"] = None
	created: Optional["integer"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	author_id: Optional["integer"] = None
	question: Optional["string"] = None
	background: Optional["pollsbackground"] = None
	votes: Optional["integer"] = None
	disable_unvote: Optional["boolean"] = None


PollsPollAnonymous = Optional[bool] # Information whether the field is anonymous



class PollsVoters(BaseModel):
	"""VK Object PollsVoters

	answer_id - Answer ID
	users - 
	"""
	answer_id: Optional["integer"] = None
	users: Optional["pollsvotersusers"] = None


class PollsVotersUsers(BaseModel):
	"""VK Object PollsVotersUsers

	count - Votes number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["integer"] = None


class PrettyCardsPrettycard(BaseModel):
	"""VK Object PrettyCardsPrettycard

	button - Button key
	button_text - Button text in current language
	card_id - Card ID (long int returned as string)
	images - 
	link_url - Link URL
	photo - Photo ID (format "<owner_id>_<media_id>")
	price - Price if set (decimal number returned as string)
	price_old - Old price if set (decimal number returned as string)
	title - Title
	"""
	button: Optional["string"] = None
	button_text: Optional["string"] = None
	card_id: Optional["string"] = None
	images: Optional["baseimage"] = None
	link_url: Optional["string"] = None
	photo: Optional["string"] = None
	price: Optional["string"] = None
	price_old: Optional["string"] = None
	title: Optional["string"] = None


class SearchHint(BaseModel):
	"""VK Object SearchHint

	app - 
	description - Object description
	global - Information whether the object has been found globally
	group - 
	profile - 
	section - 
	type - 
	"""
	app: Optional["appsapp"] = None
	description: Optional["string"] = None
	global: Optional["baseboolint"] = None
	group: Optional["groupsgroup"] = None
	profile: Optional["usersusermin"] = None
	section: Optional["searchhintsection"] = None
	type: Optional["searchhinttype"] = None


class SearchHintSection(enum.Enum):
	"""VK Object SearchHintSection

	"""
	GROUPS = "groups"
	EVENTS = "events"
	PUBLICS = "publics"
	CORRESPONDENTS = "correspondents"
	PEOPLE = "people"
	FRIENDS = "friends"
	MUTUAL_FRIENDS = "mutual_friends"


class SearchHintType(enum.Enum):
	"""VK Object SearchHintType

	"""
	GROUP = "group"
	PROFILE = "profile"
	VK_APP = "vk_app"
	APP = "app"
	HTML5_GAME = "html5_game"


class SecureLevel(BaseModel):
	"""VK Object SecureLevel

	level - Level
	uid - User ID
	"""
	level: Optional["integer"] = None
	uid: Optional["integer"] = None


class SecureSmsNotification(BaseModel):
	"""VK Object SecureSmsNotification

	app_id - Application ID
	date - Date when message has been sent in Unixtime
	id - Notification ID
	message - Messsage text
	user_id - User ID
	"""
	app_id: Optional["string"] = None
	date: Optional["string"] = None
	id: Optional["string"] = None
	message: Optional["string"] = None
	user_id: Optional["string"] = None


class SecureTokenChecked(BaseModel):
	"""VK Object SecureTokenChecked

	date - Date when access_token has been generated in Unixtime
	expire - Date when access_token will expire in Unixtime
	success - Returns if successfully processed
	user_id - User ID
	"""
	date: Optional["integer"] = None
	expire: Optional["integer"] = None
	success: Optional["integer"] = None
	user_id: Optional["integer"] = None


class SecureTransaction(BaseModel):
	"""VK Object SecureTransaction

	date - Transaction date in Unixtime
	id - Transaction ID
	uid_from - From ID
	uid_to - To ID
	votes - Votes number
	"""
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	uid_from: Optional["integer"] = None
	uid_to: Optional["integer"] = None
	votes: Optional["integer"] = None


class StatsActivity(BaseModel):
	"""VK Object StatsActivity

	comments - Comments number
	copies - Reposts number
	hidden - Hidden from news count
	likes - Likes number
	subscribed - New subscribers count
	unsubscribed - Unsubscribed count
	"""
	comments: Optional["integer"] = None
	copies: Optional["integer"] = None
	hidden: Optional["integer"] = None
	likes: Optional["integer"] = None
	subscribed: Optional["integer"] = None
	unsubscribed: Optional["integer"] = None


class StatsCity(BaseModel):
	"""VK Object StatsCity

	count - Visitors number
	name - City name
	value - City ID
	"""
	count: Optional["integer"] = None
	name: Optional["string"] = None
	value: Optional["integer"] = None


class StatsCountry(BaseModel):
	"""VK Object StatsCountry

	code - Country code
	count - Visitors number
	name - Country name
	value - Country ID
	"""
	code: Optional["string"] = None
	count: Optional["integer"] = None
	name: Optional["string"] = None
	value: Optional["integer"] = None


class StatsPeriod(BaseModel):
	"""VK Object StatsPeriod

	activity - 
	period_from - Unix timestamp
	period_to - Unix timestamp
	reach - 
	visitors - 
	"""
	activity: Optional["statsactivity"] = None
	period_from: Optional["integer"] = None
	period_to: Optional["integer"] = None
	reach: Optional["statsreach"] = None
	visitors: Optional["statsviews"] = None


class StatsReach(BaseModel):
	"""VK Object StatsReach

	age - 
	cities - 
	countries - 
	mobile_reach - Reach count from mobile devices
	reach - Reach count
	reach_subscribers - Subscribers reach count
	sex - 
	sex_age - 
	"""
	age: Optional["statssexage"] = None
	cities: Optional["statscity"] = None
	countries: Optional["statscountry"] = None
	mobile_reach: Optional["integer"] = None
	reach: Optional["integer"] = None
	reach_subscribers: Optional["integer"] = None
	sex: Optional["statssexage"] = None
	sex_age: Optional["statssexage"] = None


class StatsSexAge(BaseModel):
	"""VK Object StatsSexAge

	count - Visitors number
	value - Sex/age value
	reach - 
	reach_subscribers - 
	count_subscribers - 
	"""
	count: Optional["integer"] = None
	value: Optional["string"] = None
	reach: Optional["integer"] = None
	reach_subscribers: Optional["integer"] = None
	count_subscribers: Optional["integer"] = None


class StatsViews(BaseModel):
	"""VK Object StatsViews

	age - 
	cities - 
	countries - 
	mobile_views - Number of views from mobile devices
	sex - 
	sex_age - 
	views - Views number
	visitors - Visitors number
	"""
	age: Optional["statssexage"] = None
	cities: Optional["statscity"] = None
	countries: Optional["statscountry"] = None
	mobile_views: Optional["integer"] = None
	sex: Optional["statssexage"] = None
	sex_age: Optional["statssexage"] = None
	views: Optional["integer"] = None
	visitors: Optional["integer"] = None


class StatsWallpostStat(BaseModel):
	"""VK Object StatsWallpostStat

	post_id - 
	hide - Hidings number
	join_group - People have joined the group
	links - Link clickthrough
	reach_subscribers - Subscribers reach
	reach_subscribers_count - 
	reach_total - Total reach
	reach_total_count - 
	reach_viral - 
	reach_ads - 
	report - Reports number
	to_group - Clickthrough to community
	unsubscribe - Unsubscribed members
	sex_age - 
	"""
	post_id: Optional["integer"] = None
	hide: Optional["integer"] = None
	join_group: Optional["integer"] = None
	links: Optional["integer"] = None
	reach_subscribers: Optional["integer"] = None
	reach_subscribers_count: Optional["integer"] = None
	reach_total: Optional["integer"] = None
	reach_total_count: Optional["integer"] = None
	reach_viral: Optional["integer"] = None
	reach_ads: Optional["integer"] = None
	report: Optional["integer"] = None
	to_group: Optional["integer"] = None
	unsubscribe: Optional["integer"] = None
	sex_age: Optional["statssexage"] = None


class StatusStatus(BaseModel):
	"""VK Object StatusStatus

	text - Status text
	audio - 
	"""
	text: Optional["string"] = None
	audio: Optional["audioaudio"] = None


class StickersImageSet(BaseModel):
	"""VK Object StickersImageSet

	base_url - Base URL for images in set
	version - Version number to be appended to the image URL
	"""
	base_url: Optional["string"] = None
	version: Optional["integer"] = None


class StorageValue(BaseModel):
	"""VK Object StorageValue

	"""
	key: Optional["string"] = None
	value: Optional["string"] = None


class StoreProduct(BaseModel):
	"""VK Object StoreProduct

	id - Id of the product
	type - Product type
	purchased - Information whether the product is purchased (1 - yes, 0 - no)
	active - Information whether the product is active (1 - yes, 0 - no)
	promoted - Information whether the product is promoted (1 - yes, 0 - no)
	purchase_date - Date (Unix time) when the product was purchased
	title - Title of the product
	stickers - 
	icon - Array of icon images or icon set object of the product (for stickers product type)
	previews - Array of preview images of the product (for stickers product type)
	has_animation - Information whether the product is an animated sticker pack (for stickers product type)
	subtitle - Subtitle of the product
	"""
	id: Optional["integer"] = None
	type: Optional["string"] = None
	purchased: Optional["baseboolint"] = None
	active: Optional["baseboolint"] = None
	promoted: Optional["baseboolint"] = None
	purchase_date: Optional["integer"] = None
	title: Optional["string"] = None
	stickers: Optional["basestickerslist"] = None
	icon: Optional["storeproducticon"] = None
	previews: Optional["baseimage"] = None
	has_animation: Optional["boolean"] = None
	subtitle: Optional["string"] = None
None

class StoreStickersKeyword(BaseModel):
	"""VK Object StoreStickersKeyword

	"""
	words: Optional["string"] = None
	user_stickers: Optional["storestickerskeywordstickers"] = None
	promoted_stickers: Optional["storestickerskeywordstickers"] = None
	stickers: Optional["storestickerskeywordsticker"] = None


class StoreStickersKeywordSticker(BaseModel):
	"""VK Object StoreStickersKeywordSticker

	pack_id - Pack id
	sticker_id - Sticker id
	"""
	pack_id: Optional["integer"] = None
	sticker_id: Optional["integer"] = None


class StoreStickersKeywordStickers(BaseModel):
	"""VK Object StoreStickersKeywordStickers

	"""


class StoriesClickableArea(BaseModel):
	"""VK Object StoriesClickableArea

	"""
	x: Optional["integer"] = None
	y: Optional["integer"] = None


class StoriesClickableSticker(BaseModel):
	"""VK Object StoriesClickableSticker

	clickable_area - 
	id - Clickable sticker ID
	hashtag - 
	link_object - 
	mention - 
	tooltip_text - 
	owner_id - 
	story_id - 
	question - 
	question_button - 
	place_id - 
	market_item - 
	audio - 
	audio_start_time - 
	style - 
	type - 
	subtype - 
	post_owner_id - 
	post_id - 
	poll - 
	color - Color, hex format
	sticker_id - Sticker ID
	sticker_pack_id - Sticker pack ID
	app - 
	app_context - Additional context for app sticker
	has_new_interactions - Whether current user has unread interaction with this app
	is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
	situational_theme_id - 
	situational_app_url - 
	"""
	clickable_area: Optional["storiesclickablearea"] = None
	id: Optional["integer"] = None
	hashtag: Optional["string"] = None
	link_object: Optional["baselink"] = None
	mention: Optional["string"] = None
	tooltip_text: Optional["string"] = None
	owner_id: Optional["integer"] = None
	story_id: Optional["integer"] = None
	question: Optional["string"] = None
	question_button: Optional["string"] = None
	place_id: Optional["integer"] = None
	market_item: Optional["marketmarketitem"] = None
	audio: Optional["audioaudio"] = None
	audio_start_time: Optional["integer"] = None
	style: Optional["string"] = None
	type: Optional["string"] = None
	subtype: Optional["string"] = None
	post_owner_id: Optional["integer"] = None
	post_id: Optional["integer"] = None
	poll: Optional["pollspoll"] = None
	color: Optional["string"] = None
	sticker_id: Optional["integer"] = None
	sticker_pack_id: Optional["integer"] = None
	app: Optional["appsappmin"] = None
	app_context: Optional["string"] = None
	has_new_interactions: Optional["boolean"] = None
	is_broadcast_notify_allowed: Optional["boolean"] = None
	situational_theme_id: Optional["integer"] = None
	situational_app_url: Optional["string"] = None


class StoriesClickableStickers(BaseModel):
	"""VK Object StoriesClickableStickers

	"""
	clickable_stickers: Optional["storiesclickablesticker"] = None
	original_height: Optional["integer"] = None
	original_width: Optional["integer"] = None


class StoriesFeedItem(BaseModel):
	"""VK Object StoriesFeedItem

	type - Type of Feed Item
	id - 
	stories - Author stories
	grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
	app - App, which stories has been grouped (for type app_grouped_stories)
	promo_data - Additional data for promo stories (for type promo_stories)
	birthday_user_id - 
	"""
	type: Optional["string"] = None
	id: Optional["string"] = None
	stories: Optional["storiesstory"] = None
	grouped: Optional["storiesfeeditem"] = None
	app: Optional["appsappmin"] = None
	promo_data: Optional["storiespromoblock"] = None
	birthday_user_id: Optional["integer"] = None


class StoriesPromoBlock(BaseModel):
	"""VK Object StoriesPromoBlock

	name - Promo story title
	photo_50 - RL of square photo of the story with 50 pixels in width
	photo_100 - RL of square photo of the story with 100 pixels in width
	not_animated - Hide animation for promo story
	"""
	name: Optional["string"] = None
	photo_50: Optional["string"] = None
	photo_100: Optional["string"] = None
	not_animated: Optional["boolean"] = None


class StoriesReplies(BaseModel):
	"""VK Object StoriesReplies

	count - Replies number.
	new - New replies number.
	"""
	count: Optional["integer"] = None
	new: Optional["integer"] = None


class StoriesStatLine(BaseModel):
	"""VK Object StoriesStatLine

	"""
	name: Optional["string"] = None
	counter: Optional["integer"] = None
	is_unavailable: Optional["boolean"] = None


class StoriesStory(BaseModel):
	"""VK Object StoriesStory

	access_key - Access key for private object.
	can_comment - Information whether current user can comment the story (0 - no, 1 - yes).
	can_reply - Information whether current user can reply to the story (0 - no, 1 - yes).
	can_see - Information whether current user can see the story (0 - no, 1 - yes).
	can_like - Information whether current user can like the story.
	can_share - Information whether current user can share the story (0 - no, 1 - yes).
	can_hide - Information whether current user can hide the story (0 - no, 1 - yes).
	date - Date when story has been added in Unixtime.
	expires_at - Story expiration time. Unixtime.
	id - Story ID.
	is_deleted - Information whether the story is deleted (false - no, true - yes).
	is_expired - Information whether the story is expired (false - no, true - yes).
	link - 
	owner_id - Story owner's ID.
	parent_story - 
	parent_story_access_key - Access key for private object.
	parent_story_id - Parent story ID.
	parent_story_owner_id - Parent story owner's ID.
	photo - 
	replies - Replies counters to current story.
	seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
	type - 
	clickable_stickers - 
	video - 
	views - Views number.
	can_ask - Information whether story has question sticker and current user can send question to the author
	can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
	narratives_count - 
	first_narrative_title - 
	birthday_wish_user_id - 
	can_use_in_narrative - 
	"""
	access_key: Optional["string"] = None
	can_comment: Optional["baseboolint"] = None
	can_reply: Optional["baseboolint"] = None
	can_see: Optional["baseboolint"] = None
	can_like: Optional["boolean"] = None
	can_share: Optional["baseboolint"] = None
	can_hide: Optional["baseboolint"] = None
	date: Optional["integer"] = None
	expires_at: Optional["integer"] = None
	id: Optional["integer"] = None
	is_deleted: Optional["boolean"] = None
	is_expired: Optional["boolean"] = None
	link: Optional["storiesstorylink"] = None
	owner_id: Optional["integer"] = None
	parent_story: Optional["storiesstory"] = None
	parent_story_access_key: Optional["string"] = None
	parent_story_id: Optional["integer"] = None
	parent_story_owner_id: Optional["integer"] = None
	photo: Optional["photosphoto"] = None
	replies: Optional["storiesreplies"] = None
	seen: Optional["baseboolint"] = None
	type: Optional["storiesstorytype"] = None
	clickable_stickers: Optional["storiesclickablestickers"] = None
	video: Optional["videovideo"] = None
	views: Optional["integer"] = None
	can_ask: Optional["baseboolint"] = None
	can_ask_anonymous: Optional["baseboolint"] = None
	narratives_count: Optional["integer"] = None
	first_narrative_title: Optional["string"] = None
	birthday_wish_user_id: Optional["integer"] = None
	can_use_in_narrative: Optional["boolean"] = None


class StoriesStoryLink(BaseModel):
	"""VK Object StoriesStoryLink

	text - Link text
	url - Link URL
	"""
	text: Optional["string"] = None
	url: Optional["string"] = None


class StoriesStoryStats(BaseModel):
	"""VK Object StoriesStoryStats

	"""
	answer: Optional["storiesstorystatsstat"] = None
	bans: Optional["storiesstorystatsstat"] = None
	open_link: Optional["storiesstorystatsstat"] = None
	replies: Optional["storiesstorystatsstat"] = None
	shares: Optional["storiesstorystatsstat"] = None
	subscribers: Optional["storiesstorystatsstat"] = None
	views: Optional["storiesstorystatsstat"] = None
	likes: Optional["storiesstorystatsstat"] = None


class StoriesStoryStatsStat(BaseModel):
	"""VK Object StoriesStoryStatsStat

	count - Stat value
	state - 
	"""
	count: Optional["integer"] = None
	state: Optional["storiesstorystatsstate"] = None


class StoriesStoryStatsState(enum.Enum):
	"""VK Object StoriesStoryStatsState

	"""
	ON = "on"
	OFF = "off"
	HIDDEN = "hidden"


class StoriesStoryType(enum.Enum):
	"""VK Object StoriesStoryType

	"""
	PHOTO = "photo"
	VIDEO = "video"
	LIVE_ACTIVE = "live_active"
	LIVE_FINISHED = "live_finished"
	BIRTHDAY_INVITE = "birthday_invite"


class StoriesUploadLinkText(enum.Enum):
	"""VK Object StoriesUploadLinkText

	"""
	TO_STORE = "to_store"
	VOTE = "vote"
	MORE = "more"
	BOOK = "book"
	ORDER = "order"
	ENROLL = "enroll"
	FILL = "fill"
	SIGNUP = "signup"
	BUY = "buy"
	TICKET = "ticket"
	WRITE = "write"
	OPEN = "open"
	LEARN_MORE = "learn_more"
	VIEW = "view"
	GO_TO = "go_to"
	CONTACT = "contact"
	WATCH = "watch"
	PLAY = "play"
	INSTALL = "install"
	READ = "read"
	CALENDAR = "calendar"


class StoriesViewersItem(BaseModel):
	"""VK Object StoriesViewersItem

	is_liked - user has like for this object
	user_id - user id
	user - 
	"""
	is_liked: Optional["boolean"] = None
	user_id: Optional["integer"] = None
	user: Optional["usersuserfull"] = None


class UsersCareer(BaseModel):
	"""VK Object UsersCareer

	city_id - City ID
	city_name - City name
	company - Company name
	country_id - Country ID
	from - From year
	group_id - Community ID
	id - Career ID
	position - Position
	until - Till year
	"""
	city_id: Optional["integer"] = None
	city_name: Optional["string"] = None
	company: Optional["string"] = None
	country_id: Optional["integer"] = None
	from: Optional["integer"] = None
	group_id: Optional["integer"] = None
	id: Optional["integer"] = None
	position: Optional["string"] = None
	until: Optional["integer"] = None


class UsersExports(BaseModel):
	"""VK Object UsersExports

	"""
	facebook: Optional["integer"] = None
	livejournal: Optional["integer"] = None
	twitter: Optional["integer"] = None


class UsersFields(enum.Enum):
	"""VK Object UsersFields

	"""
	FIRST_NAME_NOM = "first_name_nom"
	FIRST_NAME_GEN = "first_name_gen"
	FIRST_NAME_DAT = "first_name_dat"
	FIRST_NAME_ACC = "first_name_acc"
	FIRST_NAME_INS = "first_name_ins"
	FIRST_NAME_ABL = "first_name_abl"
	LAST_NAME_NOM = "last_name_nom"
	LAST_NAME_GEN = "last_name_gen"
	LAST_NAME_DAT = "last_name_dat"
	LAST_NAME_ACC = "last_name_acc"
	LAST_NAME_INS = "last_name_ins"
	LAST_NAME_ABL = "last_name_abl"
	PHOTO_ID = "photo_id"
	VERIFIED = "verified"
	SEX = "sex"
	BDATE = "bdate"
	CITY = "city"
	COUNTRY = "country"
	HOME_TOWN = "home_town"
	HAS_PHOTO = "has_photo"
	PHOTO_50 = "photo_50"
	PHOTO_100 = "photo_100"
	PHOTO_200_ORIG = "photo_200_orig"
	PHOTO_200 = "photo_200"
	PHOTO_400 = "photo_400"
	PHOTO_400_ORIG = "photo_400_orig"
	PHOTO_MAX = "photo_max"
	PHOTO_MAX_ORIG = "photo_max_orig"
	PHOTO_MAX_SIZE = "photo_max_size"
	ONLINE = "online"
	LISTS = "lists"
	DOMAIN = "domain"
	HAS_MOBILE = "has_mobile"
	CONTACTS = "contacts"
	SITE = "site"
	EDUCATION = "education"
	UNIVERSITIES = "universities"
	SCHOOLS = "schools"
	STATUS = "status"
	LAST_SEEN = "last_seen"
	FOLLOWERS_COUNT = "followers_count"
	COUNTERS = "counters"
	COMMON_COUNT = "common_count"
	OCCUPATION = "occupation"
	NICKNAME = "nickname"
	RELATIVES = "relatives"
	RELATION = "relation"
	PERSONAL = "personal"
	CONNECTIONS = "connections"
	EXPORTS = "exports"
	WALL_COMMENTS = "wall_comments"
	ACTIVITIES = "activities"
	INTERESTS = "interests"
	MUSIC = "music"
	MOVIES = "movies"
	TV = "tv"
	BOOKS = "books"
	GAMES = "games"
	ABOUT = "about"
	QUOTES = "quotes"
	CAN_POST = "can_post"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_SEE_AUDIO = "can_see_audio"
	CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
	CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
	IS_FAVORITE = "is_favorite"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	TIMEZONE = "timezone"
	SCREEN_NAME = "screen_name"
	MAIDEN_NAME = "maiden_name"
	CROP_PHOTO = "crop_photo"
	IS_FRIEND = "is_friend"
	FRIEND_STATUS = "friend_status"
	CAREER = "career"
	MILITARY = "military"
	BLACKLISTED = "blacklisted"
	BLACKLISTED_BY_ME = "blacklisted_by_me"
	CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
	DESCRIPTIONS = "descriptions"
	TRENDING = "trending"
	MUTUAL = "mutual"
	FRIENDSHIP_WEEKS = "friendship_weeks"
	CAN_INVITE_TO_CHATS = "can_invite_to_chats"
	STORIES_ARCHIVE_COUNT = "stories_archive_count"
	VIDEO_LIVE_LEVEL = "video_live_level"
	VIDEO_LIVE_COUNT = "video_live_count"
	CLIPS_COUNT = "clips_count"
	SERVICE_DESCRIPTION = "service_description"
	IS_DEAD = "is_dead"


class UsersLastSeen(BaseModel):
	"""VK Object UsersLastSeen

	platform - Type of the platform that used for the last authorization
	time - Last visit date (in Unix time)
	"""
	platform: Optional["integer"] = None
	time: Optional["integer"] = None


class UsersMilitary(BaseModel):
	"""VK Object UsersMilitary

	country_id - Country ID
	from - From year
	id - Military ID
	unit - Unit name
	unit_id - Unit ID
	until - Till year
	"""
	country_id: Optional["integer"] = None
	from: Optional["integer"] = None
	id: Optional["integer"] = None
	unit: Optional["string"] = None
	unit_id: Optional["integer"] = None
	until: Optional["integer"] = None


class UsersOccupation(BaseModel):
	"""VK Object UsersOccupation

	id - ID of school, university, company group
	name - Name of occupation
	type - Type of occupation
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	type: Optional["string"] = None


class UsersOnlineInfo(BaseModel):
	"""VK Object UsersOnlineInfo

	visible - Whether you can see real online status of user or not
	last_seen - Last time we saw user being active
	is_online - Whether user is currently online or not
	app_id - Application id from which user is currently online or was last seen online
	is_mobile - Is user online from desktop app or mobile app
	status - In case user online is not visible, it indicates approximate timeframe of user online
	"""
	visible: Optional["boolean"] = None
	last_seen: Optional["integer"] = None
	is_online: Optional["boolean"] = None
	app_id: Optional["integer"] = None
	is_mobile: Optional["boolean"] = None
	status: Optional["string"] = None


class UsersPersonal(BaseModel):
	"""VK Object UsersPersonal

	alcohol - User's views on alcohol
	inspired_by - User's inspired by
	langs - 
	life_main - User's personal priority in life
	people_main - User's personal priority in people
	political - User's political views
	religion - User's religion
	religion_id - User's religion id
	smoking - User's views on smoking
	"""
	alcohol: Optional["integer"] = None
	inspired_by: Optional["string"] = None
	langs: Optional["string"] = None
	life_main: Optional["integer"] = None
	people_main: Optional["integer"] = None
	political: Optional["integer"] = None
	religion: Optional["string"] = None
	religion_id: Optional["integer"] = None
	smoking: Optional["integer"] = None


class UsersRelative(BaseModel):
	"""VK Object UsersRelative

	birth_date - Date of child birthday (format dd.mm.yyyy)
	id - Relative ID
	name - Name of relative
	type - Relative type
	"""
	birth_date: Optional["string"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None
	type: Optional["string"] = None


class UsersSchool(BaseModel):
	"""VK Object UsersSchool

	city - City ID
	class - School class letter
	country - Country ID
	id - School ID
	name - School name
	type - School type ID
	type_str - School type name
	year_from - Year the user started to study
	year_graduated - Graduation year
	year_to - Year the user finished to study
	speciality - 
	"""
	city: Optional["integer"] = None
	class: Optional["string"] = None
	country: Optional["integer"] = None
	id: Optional["string"] = None
	name: Optional["string"] = None
	type: Optional["integer"] = None
	type_str: Optional["string"] = None
	year_from: Optional["integer"] = None
	year_graduated: Optional["integer"] = None
	year_to: Optional["integer"] = None
	speciality: Optional["string"] = None


class UsersSubscriptionsItem(BaseModel):
	"""VK Object UsersSubscriptionsItem

	"""


class UsersUniversity(BaseModel):
	"""VK Object UsersUniversity

	chair - Chair ID
	chair_name - Chair name
	city - City ID
	country - Country ID
	education_form - Education form
	education_status - Education status
	faculty - Faculty ID
	faculty_name - Faculty name
	graduation - Graduation year
	id - University ID
	name - University name
	university_group_id - 
	"""
	chair: Optional["integer"] = None
	chair_name: Optional["string"] = None
	city: Optional["integer"] = None
	country: Optional["integer"] = None
	education_form: Optional["string"] = None
	education_status: Optional["string"] = None
	faculty: Optional["integer"] = None
	faculty_name: Optional["string"] = None
	graduation: Optional["integer"] = None
	id: Optional["integer"] = None
	name: Optional["string"] = None
	university_group_id: Optional["integer"] = None


class UsersUser(UsersUserMin):
	"""VK Object UsersUser

	sex - User sex
	screen_name - Domain name of the user's page
	photo_50 - URL of square photo of the user with 50 pixels in width
	photo_100 - URL of square photo of the user with 100 pixels in width
	online_info - 
	online - Information whether the user is online
	online_mobile - Information whether the user is online in mobile site or application
	online_app - Application ID
	verified - Information whether the user is verified
	trending - Information whether the user has a "fire" pictogram.
	friend_status - 
	mutual - 
	"""
	sex = None
	screen_name = None
	photo_50 = None
	photo_100 = None
	online_info = None
	online = None
	online_mobile = None
	online_app = None
	verified = None
	trending = None
	friend_status = None
	mutual = None


class UsersUserConnections(BaseModel):
	"""VK Object UsersUserConnections

	skype - User's Skype nickname
	facebook - User's Facebook account
	facebook_name - User's Facebook name
	twitter - User's Twitter account
	livejournal - User's Livejournal account
	instagram - User's Instagram account
	"""
	skype: Optional["string"] = None
	facebook: Optional["string"] = None
	facebook_name: Optional["string"] = None
	twitter: Optional["string"] = None
	livejournal: Optional["string"] = None
	instagram: Optional["string"] = None


class UsersUserCounters(BaseModel):
	"""VK Object UsersUserCounters

	albums - Albums number
	audios - Audios number
	followers - Followers number
	friends - Friends number
	gifts - Gifts number
	groups - Communities number
	notes - Notes number
	online_friends - Online friends number
	pages - Public pages number
	photos - Photos number
	subscriptions - Subscriptions number
	user_photos - Number of photos with user
	user_videos - Number of videos with user
	videos - Videos number
	new_photo_tags - 
	new_recognition_tags - 
	mutual_friends - 
	posts - 
	articles - 
	wishes - 
	podcasts - 
	clips - 
	clips_followers - 
	"""
	albums: Optional["integer"] = None
	audios: Optional["integer"] = None
	followers: Optional["integer"] = None
	friends: Optional["integer"] = None
	gifts: Optional["integer"] = None
	groups: Optional["integer"] = None
	notes: Optional["integer"] = None
	online_friends: Optional["integer"] = None
	pages: Optional["integer"] = None
	photos: Optional["integer"] = None
	subscriptions: Optional["integer"] = None
	user_photos: Optional["integer"] = None
	user_videos: Optional["integer"] = None
	videos: Optional["integer"] = None
	new_photo_tags: Optional["integer"] = None
	new_recognition_tags: Optional["integer"] = None
	mutual_friends: Optional["integer"] = None
	posts: Optional["integer"] = None
	articles: Optional["integer"] = None
	wishes: Optional["integer"] = None
	podcasts: Optional["integer"] = None
	clips: Optional["integer"] = None
	clips_followers: Optional["integer"] = None


class UsersUserFull(UsersUser):
	"""VK Object UsersUserFull

	first_name_nom - User's first name in nominative case
	first_name_gen - User's first name in genitive case
	first_name_dat - User's first name in dative case
	first_name_acc - User's first name in accusative case
	first_name_ins - User's first name in instrumental case
	first_name_abl - User's first name in prepositional case
	last_name_nom - User's last name in nominative case
	last_name_gen - User's last name in genitive case
	last_name_dat - User's last name in dative case
	last_name_acc - User's last name in accusative case
	last_name_ins - User's last name in instrumental case
	last_name_abl - User's last name in prepositional case
	nickname - User nickname
	maiden_name - User maiden name
	contact_name - User contact name
	domain - Domain name of the user's page
	bdate - User's date of birth
	city - 
	country - 
	timezone - User's timezone
	owner_state - 
	photo_200 - URL of square photo of the user with 200 pixels in width
	photo_max - URL of square photo of the user with maximum width
	photo_200_orig - URL of user's photo with 200 pixels in width
	photo_400_orig - URL of user's photo with 400 pixels in width
	photo_max_orig - URL of user's photo of maximum size
	photo_id - ID of the user's main photo
	has_photo - Information whether the user has main photo
	has_mobile - Information whether the user specified his phone number
	is_friend - Information whether the user is a friend of current user
	wall_comments - Information whether current user can comment wall posts
	can_post - Information whether current user can post on the user's wall
	can_see_all_posts - Information whether current user can see other users' audio on the wall
	can_see_audio - Information whether current user can see the user's audio
	type - 
	email - 
	skype - 
	facebook - 
	facebook_name - 
	twitter - 
	livejournal - 
	instagram - 
	test - 
	video_live - 
	is_video_live_notifications_blocked - 
	is_service - 
	service_description - 
	photo_rec - 
	photo_medium - 
	photo_medium_rec - 
	photo - 
	photo_big - 
	photo_400 - 
	photo_max_size - 
	language - 
	stories_archive_count - 
	wall_default - 
	can_call - Information whether current user can call
	can_see_wishes - Information whether current user can see the user's wishes
	can_see_gifts - Information whether current user can see the user's gifts
	interests - 
	books - 
	tv - 
	quotes - 
	about - 
	games - 
	movies - 
	activities - 
	music - 
	can_write_private_message - Information whether current user can write private message
	can_send_friend_request - Information whether current user can send a friend request
	can_be_invited_group - Information whether current user can be invited to the community
	mobile_phone - User's mobile phone number
	home_phone - User's additional phone number
	site - User's website
	status_audio - 
	status - User's status
	activity - User's status
	last_seen - 
	exports - 
	crop_photo - 
	followers_count - Number of user's followers
	video_live_level - User level in live streams achievements
	video_live_count - Number of user's live streams
	clips_count - Number of user's clips
	blacklisted - Information whether current user is in the requested user's blacklist.
	blacklisted_by_me - Information whether the requested user is in current user's blacklist
	is_favorite - Information whether the requested user is in faves of current user
	is_hidden_from_feed - Information whether the requested user is hidden from current user's newsfeed
	common_count - Number of common friends with current user
	occupation - 
	career - 
	military - 
	university - University ID
	university_name - University name
	university_group_id - 
	faculty - Faculty ID
	faculty_name - Faculty name
	graduation - Graduation year
	education_form - Education form
	education_status - User's education status
	home_town - User hometown
	relation - User relationship status
	relation_partner - 
	personal - 
	universities - 
	schools - 
	relatives - 
	is_subscribed_podcasts - Information whether current user is subscribed to podcasts
	can_subscribe_podcasts - Owner in whitelist or not
	can_subscribe_posts - Can subscribe to wall
	counters - 
	access_key - 
	can_upload_doc - 
	hash - 
	has_email - 
	"""
	first_name_nom = None
	first_name_gen = None
	first_name_dat = None
	first_name_acc = None
	first_name_ins = None
	first_name_abl = None
	last_name_nom = None
	last_name_gen = None
	last_name_dat = None
	last_name_acc = None
	last_name_ins = None
	last_name_abl = None
	nickname = None
	maiden_name = None
	contact_name = None
	domain = None
	bdate = None
	city = None
	country = None
	timezone = None
	owner_state = None
	photo_200 = None
	photo_max = None
	photo_200_orig = None
	photo_400_orig = None
	photo_max_orig = None
	photo_id = None
	has_photo = None
	has_mobile = None
	is_friend = None
	wall_comments = None
	can_post = None
	can_see_all_posts = None
	can_see_audio = None
	type = None
	email = None
	skype = None
	facebook = None
	facebook_name = None
	twitter = None
	livejournal = None
	instagram = None
	test = None
	video_live = None
	is_video_live_notifications_blocked = None
	is_service = None
	service_description = None
	photo_rec = None
	photo_medium = None
	photo_medium_rec = None
	photo = None
	photo_big = None
	photo_400 = None
	photo_max_size = None
	language = None
	stories_archive_count = None
	wall_default = None
	can_call = None
	can_see_wishes = None
	can_see_gifts = None
	interests = None
	books = None
	tv = None
	quotes = None
	about = None
	games = None
	movies = None
	activities = None
	music = None
	can_write_private_message = None
	can_send_friend_request = None
	can_be_invited_group = None
	mobile_phone = None
	home_phone = None
	site = None
	status_audio = None
	status = None
	activity = None
	last_seen = None
	exports = None
	crop_photo = None
	followers_count = None
	video_live_level = None
	video_live_count = None
	clips_count = None
	blacklisted = None
	blacklisted_by_me = None
	is_favorite = None
	is_hidden_from_feed = None
	common_count = None
	occupation = None
	career = None
	military = None
	university = None
	university_name = None
	university_group_id = None
	faculty = None
	faculty_name = None
	graduation = None
	education_form = None
	education_status = None
	home_town = None
	relation = None
	relation_partner = None
	personal = None
	universities = None
	schools = None
	relatives = None
	is_subscribed_podcasts = None
	can_subscribe_podcasts = None
	can_subscribe_posts = None
	counters = None
	access_key = None
	can_upload_doc = None
	hash = None
	has_email = None


class UsersUserMin(BaseModel):
	"""VK Object UsersUserMin

	deactivated - Returns if a profile is deleted or blocked
	first_name - User first name
	hidden - Returns if a profile is hidden.
	id - User ID
	last_name - User last name
	can_access_closed - 
	is_closed - 
	"""
	deactivated: Optional["string"] = None
	first_name: Optional["string"] = None
	hidden: Optional["integer"] = None
	id: Optional["integer"] = None
	last_name: Optional["string"] = None
	can_access_closed: Optional["boolean"] = None
	is_closed: Optional["boolean"] = None


class UsersUserRelation(enum.IntEnum):
	"""VK Object UsersUserRelation

	"""
	not specified = 0
	single = 1
	in a relationship = 2
	engaged = 3
	married = 4
	complicated = 5
	actively searching = 6
	in love = 7
	in a civil union = 8


class UsersUserSettingsXtr(BaseModel):
	"""VK Object UsersUserSettingsXtr

	connections - 
	bdate - User's date of birth
	bdate_visibility - Information whether user's birthdate are hidden
	city - 
	country - 
	first_name - User first name
	home_town - User's hometown
	last_name - User last name
	maiden_name - User maiden name
	name_request - 
	personal - 
	phone - User phone number with some hidden digits
	relation - User relationship status
	relation_partner - 
	relation_pending - Information whether relation status is pending
	relation_requests - 
	screen_name - Domain name of the user's page
	sex - User sex
	status - User status
	status_audio - 
	interests - 
	languages - 
	"""
	connections: Optional["usersuserconnections"] = None
	bdate: Optional["string"] = None
	bdate_visibility: Optional["integer"] = None
	city: Optional["basecity"] = None
	country: Optional["basecountry"] = None
	first_name: Optional["string"] = None
	home_town: Optional["string"] = None
	last_name: Optional["string"] = None
	maiden_name: Optional["string"] = None
	name_request: Optional["accountnamerequest"] = None
	personal: Optional["userspersonal"] = None
	phone: Optional["string"] = None
	relation: Optional["usersuserrelation"] = None
	relation_partner: Optional["usersusermin"] = None
	relation_pending: Optional["baseboolint"] = None
	relation_requests: Optional["usersusermin"] = None
	screen_name: Optional["string"] = None
	sex: Optional["basesex"] = None
	status: Optional["string"] = None
	status_audio: Optional["audioaudio"] = None
	interests: Optional["accountusersettingsinterests"] = None
	languages: Optional["string"] = None


class UsersUserType(enum.Enum):
	"""VK Object UsersUserType

	"""
	PROFILE = "profile"


class UsersUserXtrCounters(UsersUserFull):
	"""VK Object UsersUserXtrCounters

	"""


class UsersUserXtrType(UsersUser):
	"""VK Object UsersUserXtrType

	"""
	type = None


class UsersUsersArray(BaseModel):
	"""VK Object UsersUsersArray

	count - Users number
	items - 
	"""
	count: Optional["integer"] = None
	items: Optional["integer"] = None


class UtilsDomainResolved(BaseModel):
	"""VK Object UtilsDomainResolved

	object_id - Object ID
	group_id - Group ID
	type - 
	"""
	object_id: Optional["integer"] = None
	group_id: Optional["integer"] = None
	type: Optional["utilsdomainresolvedtype"] = None


class UtilsDomainResolvedType(enum.Enum):
	"""VK Object UtilsDomainResolvedType

	"""
	USER = "user"
	GROUP = "group"
	APPLICATION = "application"
	PAGE = "page"
	VK_APP = "vk_app"
	COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
	"""VK Object UtilsLastShortenedLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	timestamp - Creation time in Unixtime
	url - Full URL
	views - Total views number
	"""
	access_key: Optional["string"] = None
	key: Optional["string"] = None
	short_url: Optional["string"] = None
	timestamp: Optional["integer"] = None
	url: Optional["string"] = None
	views: Optional["integer"] = None


class UtilsLinkChecked(BaseModel):
	"""VK Object UtilsLinkChecked

	link - Link URL
	status - 
	"""
	link: Optional["string"] = None
	status: Optional["utilslinkcheckedstatus"] = None


class UtilsLinkCheckedStatus(enum.Enum):
	"""VK Object UtilsLinkCheckedStatus

	"""
	NOT_BANNED = "not_banned"
	BANNED = "banned"
	PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
	"""VK Object UtilsLinkStats

	key - Link key (characters after vk.cc/)
	stats - 
	"""
	key: Optional["string"] = None
	stats: Optional["utilsstats"] = None


class UtilsLinkStatsExtended(BaseModel):
	"""VK Object UtilsLinkStatsExtended

	key - Link key (characters after vk.cc/)
	stats - 
	"""
	key: Optional["string"] = None
	stats: Optional["utilsstatsextended"] = None


class UtilsShortLink(BaseModel):
	"""VK Object UtilsShortLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	url - Full URL
	"""
	access_key: Optional["string"] = None
	key: Optional["string"] = None
	short_url: Optional["string"] = None
	url: Optional["string"] = None


class UtilsStats(BaseModel):
	"""VK Object UtilsStats

	timestamp - Start time
	views - Total views number
	"""
	timestamp: Optional["integer"] = None
	views: Optional["integer"] = None


class UtilsStatsCity(BaseModel):
	"""VK Object UtilsStatsCity

	city_id - City ID
	views - Views number
	"""
	city_id: Optional["integer"] = None
	views: Optional["integer"] = None


class UtilsStatsCountry(BaseModel):
	"""VK Object UtilsStatsCountry

	country_id - Country ID
	views - Views number
	"""
	country_id: Optional["integer"] = None
	views: Optional["integer"] = None


class UtilsStatsExtended(BaseModel):
	"""VK Object UtilsStatsExtended

	cities - 
	countries - 
	sex_age - 
	timestamp - Start time
	views - Total views number
	"""
	cities: Optional["utilsstatscity"] = None
	countries: Optional["utilsstatscountry"] = None
	sex_age: Optional["utilsstatssexage"] = None
	timestamp: Optional["integer"] = None
	views: Optional["integer"] = None


class UtilsStatsSexAge(BaseModel):
	"""VK Object UtilsStatsSexAge

	age_range - Age denotation
	female -  Views by female users
	male -  Views by male users
	"""
	age_range: Optional["string"] = None
	female: Optional["integer"] = None
	male: Optional["integer"] = None


class VideoLiveInfo(BaseModel):
	"""VK Object VideoLiveInfo

	"""
	enabled: Optional["baseboolint"] = None
	is_notifications_blocked: Optional["baseboolint"] = None


class VideoLiveSettings(BaseModel):
	"""VK Object VideoLiveSettings

	can_rewind - If user car rewind live or not
	is_endless - If live is endless or not
	max_duration - Max possible time for rewind
	"""
	can_rewind: Optional["baseboolint"] = None
	is_endless: Optional["baseboolint"] = None
	max_duration: Optional["integer"] = None


class VideoRestrictionButton(BaseModel):
	"""VK Object VideoRestrictionButton

	"""
	action: Optional["string"] = None
	title: Optional["string"] = None


class VideoSaveResult(BaseModel):
	"""VK Object VideoSaveResult

	access_key - Video access key
	description - Video description
	owner_id - Video owner ID
	title - Video title
	upload_url - URL for the video uploading
	video_id - Video ID
	"""
	access_key: Optional["string"] = None
	description: Optional["string"] = None
	owner_id: Optional["integer"] = None
	title: Optional["string"] = None
	upload_url: Optional["string"] = None
	video_id: Optional["integer"] = None


class VideoVideo():
	"""VK Object VideoVideo

	access_key - Video access key
	adding_date - Date when the video has been added in Unixtime
	can_comment - Information whether current user can comment the video
	can_edit - Information whether current user can edit the video
	can_like - Information whether current user can like the video
	can_repost - Information whether current user can repost the video
	can_subscribe - Information whether current user can subscribe to author of the video
	can_add_to_faves - Information whether current user can add the video to favourites
	can_add - Information whether current user can add the video
	can_attach_link - Information whether current user can attach action button to the video
	is_private - 1 if video is private
	comments - Number of comments
	date - Date when video has been uploaded in Unixtime
	description - Video description
	duration - Video duration in seconds
	image - 
	first_frame - 
	width - Video width
	height - Video height
	id - Video ID
	owner_id - Video owner ID
	user_id - Id of the user who uploaded the video if it was uploaded to a group by member
	title - Video title
	is_favorite - Whether video is added to bookmarks
	player - Video embed URL
	processing - Returns if the video is processing
	converting - 1 if  video is being converted
	restriction - 
	added - 1 if video is added to user's albums
	is_subscribed - 1 if user is subscribed to author of the video
	track_code - 
	repeat - Information whether the video is repeated
	type - 
	views - Number of views
	local_views - If video is external, number of views on vk
	content_restricted - Restriction code
	content_restricted_message - Restriction text
	balance - Live donations balance
	live_status - Live stream status
	live - 1 if the video is a live stream
	upcoming - 1 if the video is an upcoming stream
	live_start_time - Date in Unixtime when the live stream is scheduled to start by the author
	live_notify - Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)
	spectators - Number of spectators of the stream
	platform - External platform
	likes - 
	reposts - 
	"""
	access_key = None
	adding_date = None
	can_comment = None
	can_edit = None
	can_like = None
	can_repost = None
	can_subscribe = None
	can_add_to_faves = None
	can_add = None
	can_attach_link = None
	is_private = None
	comments = None
	date = None
	description = None
	duration = None
	image = None
	first_frame = None
	width = None
	height = None
	id = None
	owner_id = None
	user_id = None
	title = None
	is_favorite = None
	player = None
	processing = None
	converting = None
	restriction = None
	added = None
	is_subscribed = None
	track_code = None
	repeat = None
	type = None
	views = None
	local_views = None
	content_restricted = None
	content_restricted_message = None
	balance = None
	live_status = None
	live = None
	upcoming = None
	live_start_time = None
	live_notify = None
	spectators = None
	platform = None
	likes = None
	reposts = None


class VideoVideoAlbumFull(BaseModel):
	"""VK Object VideoVideoAlbumFull

	count - Total number of videos in album
	id - Album ID
	image - Album cover image in different sizes
	image_blur - Need blur album thumb or not
	is_system - Information whether album is system
	owner_id - Album owner's ID
	title - Album title
	updated_time - Date when the album has been updated last time in Unixtime
	"""
	count: Optional["integer"] = None
	id: Optional["integer"] = None
	image: Optional["videovideoimage"] = None
	image_blur: Optional["basepropertyexists"] = None
	is_system: Optional["basepropertyexists"] = None
	owner_id: Optional["integer"] = None
	title: Optional["string"] = None
	updated_time: Optional["integer"] = None


class VideoVideoFiles(BaseModel):
	"""VK Object VideoVideoFiles

	external - URL of the external player
	mp4_240 - URL of the mpeg4 file with 240p quality
	mp4_360 - URL of the mpeg4 file with 360p quality
	mp4_480 - URL of the mpeg4 file with 480p quality
	mp4_720 - URL of the mpeg4 file with 720p quality
	mp4_1080 - URL of the mpeg4 file with 1080p quality
	flv_320 - URL of the flv file with 320p quality
	"""
	external: Optional["string"] = None
	mp4_240: Optional["string"] = None
	mp4_360: Optional["string"] = None
	mp4_480: Optional["string"] = None
	mp4_720: Optional["string"] = None
	mp4_1080: Optional["string"] = None
	flv_320: Optional["string"] = None


class VideoVideoFull(VideoVideo):
	"""VK Object VideoVideoFull

	files - 
	live_settings - Settings for live stream
	"""
	files = None
	live_settings = None


class VideoVideoImage(BaseImage):
	"""VK Object VideoVideoImage

	"""
	with_padding = None


class WallAppPost(BaseModel):
	"""VK Object WallAppPost

	id - Application ID
	name - Application name
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id: Optional["integer"] = None
	name: Optional["string"] = None
	photo_130: Optional["string"] = None
	photo_604: Optional["string"] = None


class WallAttachedNote(BaseModel):
	"""VK Object WallAttachedNote

	comments - Comments number
	date - Date when the note has been created in Unixtime
	id - Note ID
	owner_id - Note owner's ID
	read_comments - Read comments number
	title - Note title
	view_url - URL of the page with note preview
	"""
	comments: Optional["integer"] = None
	date: Optional["integer"] = None
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	read_comments: Optional["integer"] = None
	title: Optional["string"] = None
	view_url: Optional["string"] = None


class WallCarouselBase(BaseModel):
	"""VK Object WallCarouselBase

	carousel_offset - Index of current carousel element
	"""
	carousel_offset: Optional["integer"] = None


class WallCommentAttachment(BaseModel):
	"""VK Object WallCommentAttachment

	"""
	audio: Optional["audioaudio"] = None
	doc: Optional["docsdoc"] = None
	link: Optional["baselink"] = None
	market: Optional["marketmarketitem"] = None
	market_market_album: Optional["marketmarketalbum"] = None
	note: Optional["wallattachednote"] = None
	page: Optional["pageswikipagefull"] = None
	photo: Optional["photosphoto"] = None
	sticker: Optional["basesticker"] = None
	type: Optional["wallcommentattachmenttype"] = None
	video: Optional["videovideo"] = None


class WallCommentAttachmentType(enum.Enum):
	"""VK Object WallCommentAttachmentType

	"""
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	NOTE = "note"
	PAGE = "page"
	MARKET_MARKET_ALBUM = "market_market_album"
	MARKET = "market"
	STICKER = "sticker"


class WallGeo(BaseModel):
	"""VK Object WallGeo

	coordinates - Coordinates as string. <latitude> <longtitude>
	place - 
	showmap - Information whether a map is showed
	type - Place type
	"""
	coordinates: Optional["string"] = None
	place: Optional["baseplace"] = None
	showmap: Optional["integer"] = None
	type: Optional["string"] = None


class WallGraffiti(BaseModel):
	"""VK Object WallGraffiti

	id - Graffiti ID
	owner_id - Graffiti owner's ID
	photo_200 - URL of the preview image with 200 px in width
	photo_586 - URL of the preview image with 586 px in width
	"""
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	photo_200: Optional["string"] = None
	photo_586: Optional["string"] = None


class WallPostCopyright(BaseModel):
	"""VK Object WallPostCopyright

	"""
	id: Optional["integer"] = None
	link: Optional["string"] = None
	name: Optional["string"] = None
	type: Optional["string"] = None


class WallPostSource(BaseModel):
	"""VK Object WallPostSource

	data - Additional data
	platform - Platform name
	type - 
	url - URL to an external site used to publish the post
	"""
	data: Optional["string"] = None
	platform: Optional["string"] = None
	type: Optional["wallpostsourcetype"] = None
	url: Optional["string"] = None


class WallPostSourceType(enum.Enum):
	"""VK Object WallPostSourceType

	"""
	VK = "vk"
	WIDGET = "widget"
	API = "api"
	RSS = "rss"
	SMS = "sms"
	MVK = "mvk"


class WallPostType(enum.Enum):
	"""VK Object WallPostType

	"""
	POST = "post"
	COPY = "copy"
	REPLY = "reply"
	POSTPONE = "postpone"
	SUGGEST = "suggest"


class WallPostedPhoto(BaseModel):
	"""VK Object WallPostedPhoto

	id - Photo ID
	owner_id - Photo owner's ID
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	photo_130: Optional["string"] = None
	photo_604: Optional["string"] = None


class WallViews(BaseModel):
	"""VK Object WallViews

	count - Count
	"""
	count: Optional["integer"] = None


class WallWallComment(BaseModel):
	"""VK Object WallWallComment

	attachments - 
	date - Date when the comment has been added in Unixtime
	donut - 
	from_id - Author ID
	id - Comment ID
	likes - 
	real_offset - Real position of the comment
	reply_to_comment - Replied comment ID
	reply_to_user - Replied user ID
	text - Comment text
	thread - 
	post_id - 
	owner_id - 
	parents_stack - 
	deleted - 
	"""
	attachments: Optional["wallcommentattachment"] = None
	date: Optional["integer"] = None
	donut: Optional["wallwallcommentdonut"] = None
	from_id: Optional["integer"] = None
	id: Optional["integer"] = None
	likes: Optional["baselikesinfo"] = None
	real_offset: Optional["integer"] = None
	reply_to_comment: Optional["integer"] = None
	reply_to_user: Optional["integer"] = None
	text: Optional["string"] = None
	thread: Optional["commentthread"] = None
	post_id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	parents_stack: Optional["integer"] = None
	deleted: Optional["boolean"] = None


class WallWallCommentDonut(BaseModel):
	"""VK Object WallWallCommentDonut

	is_don - Means commentator is donator
	placeholder - 
	"""
	is_don: Optional["boolean"] = None
	placeholder: Optional["wallwallcommentdonutplaceholder"] = None


class WallWallCommentDonutPlaceholder(BaseModel):
	"""VK Object WallWallCommentDonutPlaceholder

	"""
	text: Optional["string"] = None


class WallWallpost(BaseModel):
	"""VK Object WallWallpost

	access_key - Access key to private object
	attachments - 
	copyright - Information about the source of the post
	date - Date of publishing in Unixtime
	edited - Date of editing in Unixtime
	from_id - Post author ID
	geo - 
	id - Post ID
	is_archived - Is post archived, only for post owners
	is_favorite - Information whether the post in favorites list
	likes - Count of likes
	owner_id - Wall owner's ID
	poster - 
	post_id - If post type 'reply', contains original post ID
	parents_stack - If post type 'reply', contains original parent IDs stack
	post_source - 
	post_type - 
	reposts - 
	signer_id - Post signer ID
	text - Post text
	views - Count of views
	"""
	access_key: Optional["string"] = None
	attachments: Optional["wallwallpostattachment"] = None
	copyright: Optional["wallpostcopyright"] = None
	date: Optional["integer"] = None
	edited: Optional["integer"] = None
	from_id: Optional["integer"] = None
	geo: Optional["wallgeo"] = None
	id: Optional["integer"] = None
	is_archived: Optional["boolean"] = None
	is_favorite: Optional["boolean"] = None
	likes: Optional["baselikesinfo"] = None
	owner_id: Optional["integer"] = None
	poster: Optional["object"] = None
	post_id: Optional["integer"] = None
	parents_stack: Optional["integer"] = None
	post_source: Optional["wallpostsource"] = None
	post_type: Optional["wallposttype"] = None
	reposts: Optional["baserepostsinfo"] = None
	signer_id: Optional["integer"] = None
	text: Optional["string"] = None
	views: Optional["wallviews"] = None


class WallWallpostAttachment(BaseModel):
	"""VK Object WallWallpostAttachment

	access_key - Access key for the audio
	album - 
	app - 
	audio - 
	doc - 
	event - 
	group - 
	graffiti - 
	link - 
	market - 
	market_album - 
	note - 
	page - 
	photo - 
	photos_list - 
	poll - 
	posted_photo - 
	type - 
	video - 
	"""
	access_key: Optional["string"] = None
	album: Optional["photosphotoalbum"] = None
	app: Optional["wallapppost"] = None
	audio: Optional["audioaudio"] = None
	doc: Optional["docsdoc"] = None
	event: Optional["eventseventattach"] = None
	group: Optional["groupsgroupattach"] = None
	graffiti: Optional["wallgraffiti"] = None
	link: Optional["baselink"] = None
	market: Optional["marketmarketitem"] = None
	market_album: Optional["marketmarketalbum"] = None
	note: Optional["wallattachednote"] = None
	page: Optional["pageswikipagefull"] = None
	photo: Optional["photosphoto"] = None
	photos_list: Optional["string"] = None
	poll: Optional["pollspoll"] = None
	posted_photo: Optional["wallpostedphoto"] = None
	type: Optional["wallwallpostattachmenttype"] = None
	video: Optional["videovideo"] = None


class WallWallpostAttachmentType(enum.Enum):
	"""VK Object WallWallpostAttachmentType

	"""
	PHOTO = "photo"
	POSTED_PHOTO = "posted_photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	GRAFFITI = "graffiti"
	NOTE = "note"
	APP = "app"
	POLL = "poll"
	PAGE = "page"
	ALBUM = "album"
	PHOTOS_LIST = "photos_list"
	MARKET_MARKET_ALBUM = "market_market_album"
	MARKET = "market"
	EVENT = "event"


class WallWallpostCommentsDonut(BaseModel):
	"""VK Object WallWallpostCommentsDonut

	"""
	placeholder: Optional["wallwallpostcommentsdonutplaceholder"] = None


class WallWallpostCommentsDonutPlaceholder(BaseModel):
	"""VK Object WallWallpostCommentsDonutPlaceholder

	"""
	text: Optional["string"] = None


class WallWallpostDonut(BaseModel):
	"""VK Object WallWallpostDonut

	is_donut - Post only for dons
	paid_duration - Value of this field need to pass in wall.post/edit in donut_paid_duration
	placeholder - If placeholder was respond, text and all attachments will be hidden
	can_publish_free_copy - Says whether group admin can post free copy of this donut post
	edit_mode - Says what user can edit in post about donut properties
	"""
	is_donut: Optional["boolean"] = None
	paid_duration: Optional["integer"] = None
	placeholder: Optional["wallwallpostdonutplaceholder"] = None
	can_publish_free_copy: Optional["boolean"] = None
	edit_mode: Optional["string"] = None


class WallWallpostDonutPlaceholder(BaseModel):
	"""VK Object WallWallpostDonutPlaceholder

	"""
	text: Optional["string"] = None


class WallWallpostFull(WallCarouselBase,
	WallWallpost):
	"""VK Object WallWallpostFull

	copy_history - 
	can_edit - Information whether current user can edit the post
	created_by - Post creator ID (if post still can be edited)
	can_delete - Information whether current user can delete the post
	can_pin - Information whether current user can pin the post
	donut - 
	is_pinned - Information whether the post is pinned
	comments - 
	marked_as_ads - Information whether the post is marked as ads
	short_text_rate - Preview length control parameter
	"""
	copy_history = None
	can_edit = None
	created_by = None
	can_delete = None
	can_pin = None
	donut = None
	is_pinned = None
	comments = None
	marked_as_ads = None
	short_text_rate = None


class WallWallpostToId(BaseModel):
	"""VK Object WallWallpostToId

	attachments - 
	comments - 
	copy_owner_id - ID of the source post owner
	copy_post_id - ID of the source post
	date - Date of publishing in Unixtime
	from_id - Post author ID
	geo - 
	id - Post ID
	is_favorite - Information whether the post in favorites list
	likes - 
	post_id - wall post ID (if comment)
	post_source - 
	post_type - 
	reposts - 
	signer_id - Post signer ID
	text - Post text
	to_id - Wall owner's ID
	"""
	attachments: Optional["wallwallpostattachment"] = None
	comments: Optional["basecommentsinfo"] = None
	copy_owner_id: Optional["integer"] = None
	copy_post_id: Optional["integer"] = None
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	geo: Optional["wallgeo"] = None
	id: Optional["integer"] = None
	is_favorite: Optional["boolean"] = None
	likes: Optional["baselikesinfo"] = None
	post_id: Optional["integer"] = None
	post_source: Optional["wallpostsource"] = None
	post_type: Optional["wallposttype"] = None
	reposts: Optional["baserepostsinfo"] = None
	signer_id: Optional["integer"] = None
	text: Optional["string"] = None
	to_id: Optional["integer"] = None


class WidgetsCommentMedia(BaseModel):
	"""VK Object WidgetsCommentMedia

	item_id - Media item ID
	owner_id - Media owner's ID
	thumb_src - URL of the preview image (type=photo only)
	type - 
	"""
	item_id: Optional["integer"] = None
	owner_id: Optional["integer"] = None
	thumb_src: Optional["string"] = None
	type: Optional["widgetscommentmediatype"] = None


class WidgetsCommentMediaType(enum.Enum):
	"""VK Object WidgetsCommentMediaType

	"""
	AUDIO = "audio"
	PHOTO = "photo"
	VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
	"""VK Object WidgetsCommentReplies

	can_post - Information whether current user can comment the post
	count - Comments number
	replies - 
	"""
	can_post: Optional["baseboolint"] = None
	count: Optional["integer"] = None
	replies: Optional["widgetscommentrepliesitem"] = None


class WidgetsCommentRepliesItem(BaseModel):
	"""VK Object WidgetsCommentRepliesItem

	cid - Comment ID
	date - Date when the comment has been added in Unixtime
	likes - 
	text - Comment text
	uid - User ID
	user - 
	"""
	cid: Optional["integer"] = None
	date: Optional["integer"] = None
	likes: Optional["widgetswidgetlikes"] = None
	text: Optional["string"] = None
	uid: Optional["integer"] = None
	user: Optional["usersuserfull"] = None


class WidgetsWidgetComment(BaseModel):
	"""VK Object WidgetsWidgetComment

	attachments - 
	can_delete - Information whether current user can delete the comment
	comments - 
	date - Date when the comment has been added in Unixtime
	from_id - Comment author ID
	id - Comment ID
	likes - 
	media - 
	post_source - 
	post_type - Post type
	reposts - 
	text - Comment text
	to_id - Wall owner
	user - 
	"""
	attachments: Optional["wallcommentattachment"] = None
	can_delete: Optional["baseboolint"] = None
	comments: Optional["widgetscommentreplies"] = None
	date: Optional["integer"] = None
	from_id: Optional["integer"] = None
	id: Optional["integer"] = None
	likes: Optional["baselikesinfo"] = None
	media: Optional["widgetscommentmedia"] = None
	post_source: Optional["wallpostsource"] = None
	post_type: Optional["integer"] = None
	reposts: Optional["baserepostsinfo"] = None
	text: Optional["string"] = None
	to_id: Optional["integer"] = None
	user: Optional["usersuserfull"] = None


class WidgetsWidgetLikes(BaseModel):
	"""VK Object WidgetsWidgetLikes

	count - Likes number
	"""
	count: Optional["integer"] = None


class WidgetsWidgetPage(BaseModel):
	"""VK Object WidgetsWidgetPage

	comments - 
	date - Date when widgets on the page has been initialized firstly in Unixtime
	description - Page description
	id - Page ID
	likes - 
	page_id - page_id parameter value
	photo - URL of the preview image
	title - Page title
	url - Page absolute URL
	"""
	comments: Optional["baseobjectcount"] = None
	date: Optional["integer"] = None
	description: Optional["string"] = None
	id: Optional["integer"] = None
	likes: Optional["baseobjectcount"] = None
	page_id: Optional["string"] = None
	photo: Optional["string"] = None
	title: Optional["string"] = None
	url: Optional["string"] = None

AccountAccountCounters.update_forward_refs()
AccountInfo.update_forward_refs()
AccountNameRequest.update_forward_refs()
AccountNameRequestStatus.update_forward_refs()
AccountOffer.update_forward_refs()
AccountPushConversations.update_forward_refs()
AccountPushConversationsItem.update_forward_refs()
AccountPushParams.update_forward_refs()
AccountPushParamsMode.update_forward_refs()
AccountPushParamsOnoff.update_forward_refs()
AccountPushParamsSettings.update_forward_refs()
AccountPushSettings.update_forward_refs()
AccountUserSettings.update_forward_refs()
AccountUserSettingsInterest.update_forward_refs()
AccountUserSettingsInterests.update_forward_refs()
AddressesFields.update_forward_refs()
AdsAccessRole.update_forward_refs()
AdsAccessRolePublic.update_forward_refs()
AdsAccesses.update_forward_refs()
AdsAccount.update_forward_refs()
AdsAccountType.update_forward_refs()
AdsAd.update_forward_refs()
AdsAdApproved.update_forward_refs()
AdsAdCostType.update_forward_refs()
AdsAdLayout.update_forward_refs()
AdsAdStatus.update_forward_refs()
AdsCampaign.update_forward_refs()
AdsCampaignStatus.update_forward_refs()
AdsCampaignType.update_forward_refs()
AdsCategory.update_forward_refs()
AdsClient.update_forward_refs()
AdsCriteria.update_forward_refs()
AdsCriteriaSex.update_forward_refs()
AdsDemoStats.update_forward_refs()
AdsDemostatsFormat.update_forward_refs()
AdsFloodStats.update_forward_refs()
AdsLinkStatus.update_forward_refs()
AdsLookalikeRequest.update_forward_refs()
AdsLookalikeRequestSaveAudienceLevel.update_forward_refs()
AdsMusician.update_forward_refs()
AdsObjectType.update_forward_refs()
AdsParagraphs.update_forward_refs()
AdsPromotedPostReach.update_forward_refs()
AdsRejectReason.update_forward_refs()
AdsRules.update_forward_refs()
AdsStats.update_forward_refs()
AdsStatsAge.update_forward_refs()
AdsStatsCities.update_forward_refs()
AdsStatsFormat.update_forward_refs()
AdsStatsSex.update_forward_refs()
AdsStatsSexAge.update_forward_refs()
AdsStatsSexValue.update_forward_refs()
AdsStatsViewsTimes.update_forward_refs()
AdsTargSettings.update_forward_refs()
AdsTargStats.update_forward_refs()
AdsTargSuggestions.update_forward_refs()
AdsTargSuggestionsCities.update_forward_refs()
AdsTargSuggestionsRegions.update_forward_refs()
AdsTargSuggestionsSchools.update_forward_refs()
AdsTargSuggestionsSchoolsType.update_forward_refs()
AdsTargetGroup.update_forward_refs()
AdsUpdateofficeusersResult.update_forward_refs()
AdsUserSpecification.update_forward_refs()
AdsUserSpecificationCutted.update_forward_refs()
AdsUsers.update_forward_refs()
AdswebGetadcategoriesResponseCategoriesCategory.update_forward_refs()
AdswebGetadunitsResponseAdUnitsAdUnit.update_forward_refs()
AdswebGetfraudhistoryResponseEntriesEntry.update_forward_refs()
AdswebGetsitesResponseSitesSite.update_forward_refs()
AdswebGetstatisticsResponseItemsItem.update_forward_refs()
AppWidgetsPhoto.update_forward_refs()
AppWidgetsPhotos.update_forward_refs()
AppsApp.update_forward_refs()
AppsAppLeaderboardType.update_forward_refs()
AppsAppMin.update_forward_refs()
AppsAppType.update_forward_refs()
AppsLeaderboard.update_forward_refs()
AppsScope.update_forward_refs()
AudioAudio.update_forward_refs()
BaseBoolInt.update_forward_refs()
BaseCity.update_forward_refs()
BaseCommentsInfo.update_forward_refs()
BaseCountry.update_forward_refs()
BaseCropPhoto.update_forward_refs()
BaseCropPhotoCrop.update_forward_refs()
BaseCropPhotoRect.update_forward_refs()
BaseError.update_forward_refs()
BaseGeo.update_forward_refs()
BaseGeoCoordinates.update_forward_refs()
BaseGradientPoint.update_forward_refs()
BaseImage.update_forward_refs()
BaseLikes.update_forward_refs()
BaseLikesInfo.update_forward_refs()
BaseLink.update_forward_refs()
BaseLinkApplication.update_forward_refs()
BaseLinkApplicationStore.update_forward_refs()
BaseLinkButton.update_forward_refs()
BaseLinkButtonAction.update_forward_refs()
BaseLinkButtonActionType.update_forward_refs()
BaseLinkButtonStyle.update_forward_refs()
BaseLinkProduct.update_forward_refs()
BaseLinkProductStatus.update_forward_refs()
BaseLinkRating.update_forward_refs()
BaseMessageError.update_forward_refs()
BaseObject.update_forward_refs()
BaseObjectCount.update_forward_refs()
BaseObjectWithName.update_forward_refs()
BasePlace.update_forward_refs()
BasePropertyExists.update_forward_refs()
BaseRepostsInfo.update_forward_refs()
BaseRequestParam.update_forward_refs()
BaseSex.update_forward_refs()
BaseSticker.update_forward_refs()
BaseStickerAnimation.update_forward_refs()
BaseStickersList.update_forward_refs()
BaseUploadServer.update_forward_refs()
BaseUserGroupFields.update_forward_refs()
BaseUserId.update_forward_refs()
BoardDefaultOrder.update_forward_refs()
BoardTopic.update_forward_refs()
BoardTopicComment.update_forward_refs()
BoardTopicPoll.update_forward_refs()
CallbackBoardPostDelete.update_forward_refs()
CallbackConfirmationMessage.update_forward_refs()
CallbackDonutMoneyWithdraw.update_forward_refs()
CallbackDonutMoneyWithdrawError.update_forward_refs()
CallbackDonutSubscriptionCancelled.update_forward_refs()
CallbackDonutSubscriptionCreate.update_forward_refs()
CallbackDonutSubscriptionExpired.update_forward_refs()
CallbackDonutSubscriptionPriceChanged.update_forward_refs()
CallbackDonutSubscriptionProlonged.update_forward_refs()
CallbackGroupChangePhoto.update_forward_refs()
CallbackGroupChangeSettings.update_forward_refs()
CallbackGroupJoin.update_forward_refs()
CallbackGroupJoinType.update_forward_refs()
CallbackGroupLeave.update_forward_refs()
CallbackGroupMarket.update_forward_refs()
CallbackGroupOfficerRole.update_forward_refs()
CallbackGroupOfficersEdit.update_forward_refs()
CallbackGroupSettingsChanges.update_forward_refs()
CallbackLikeAddRemove.update_forward_refs()
CallbackMarketComment.update_forward_refs()
CallbackMarketCommentDelete.update_forward_refs()
CallbackMessageAllow.update_forward_refs()
CallbackMessageBase.update_forward_refs()
CallbackMessageDeny.update_forward_refs()
CallbackMessageType.update_forward_refs()
CallbackPhotoComment.update_forward_refs()
CallbackPhotoCommentDelete.update_forward_refs()
CallbackPollVoteNew.update_forward_refs()
CallbackQrScan.update_forward_refs()
CallbackUserBlock.update_forward_refs()
CallbackUserUnblock.update_forward_refs()
CallbackVideoComment.update_forward_refs()
CallbackVideoCommentDelete.update_forward_refs()
CallbackWallCommentDelete.update_forward_refs()
CallsCall.update_forward_refs()
CallsEndState.update_forward_refs()
CallsParticipants.update_forward_refs()
CommentThread.update_forward_refs()
DatabaseCity.update_forward_refs()
DatabaseFaculty.update_forward_refs()
DatabaseRegion.update_forward_refs()
DatabaseSchool.update_forward_refs()
DatabaseStation.update_forward_refs()
DatabaseUniversity.update_forward_refs()
DocsDoc.update_forward_refs()
DocsDocAttachmentType.update_forward_refs()
DocsDocPreview.update_forward_refs()
DocsDocPreviewAudioMsg.update_forward_refs()
DocsDocPreviewGraffiti.update_forward_refs()
DocsDocPreviewPhoto.update_forward_refs()
DocsDocPreviewPhotoSizes.update_forward_refs()
DocsDocPreviewVideo.update_forward_refs()
DocsDocTypes.update_forward_refs()
DonutDonatorSubscriptionInfo.update_forward_refs()
EventsEventAttach.update_forward_refs()
FaveBookmark.update_forward_refs()
FaveBookmarkType.update_forward_refs()
FavePage.update_forward_refs()
FavePageType.update_forward_refs()
FaveTag.update_forward_refs()
FriendsFriendExtendedStatus.update_forward_refs()
FriendsFriendStatus.update_forward_refs()
FriendsFriendStatusStatus.update_forward_refs()
FriendsFriendsList.update_forward_refs()
FriendsMutualFriend.update_forward_refs()
FriendsRequests.update_forward_refs()
FriendsRequestsMutual.update_forward_refs()
FriendsRequestsXtrMessage.update_forward_refs()
FriendsUserXtrLists.update_forward_refs()
FriendsUserXtrPhone.update_forward_refs()
GiftsGift.update_forward_refs()
GiftsGiftPrivacy.update_forward_refs()
GiftsLayout.update_forward_refs()
GroupsAddress.update_forward_refs()
GroupsAddressTimetable.update_forward_refs()
GroupsAddressTimetableDay.update_forward_refs()
GroupsAddressWorkInfoStatus.update_forward_refs()
GroupsAddressesInfo.update_forward_refs()
GroupsBanInfo.update_forward_refs()
GroupsBanInfoReason.update_forward_refs()
GroupsBannedItem.update_forward_refs()
GroupsCallbackServer.update_forward_refs()
GroupsCallbackSettings.update_forward_refs()
GroupsContactsItem.update_forward_refs()
GroupsCountersGroup.update_forward_refs()
GroupsCover.update_forward_refs()
GroupsFields.update_forward_refs()
GroupsFilter.update_forward_refs()
GroupsGroup.update_forward_refs()
GroupsGroupAccess.update_forward_refs()
GroupsGroupAdminLevel.update_forward_refs()
GroupsGroupAgeLimits.update_forward_refs()
GroupsGroupAttach.update_forward_refs()
GroupsGroupAudio.update_forward_refs()
GroupsGroupBanInfo.update_forward_refs()
GroupsGroupCategory.update_forward_refs()
GroupsGroupCategoryFull.update_forward_refs()
GroupsGroupCategoryType.update_forward_refs()
GroupsGroupDocs.update_forward_refs()
GroupsGroupFull.update_forward_refs()
GroupsGroupFullAgeLimits.update_forward_refs()
GroupsGroupFullMainSection.update_forward_refs()
GroupsGroupFullMemberStatus.update_forward_refs()
GroupsGroupIsClosed.update_forward_refs()
GroupsGroupLink.update_forward_refs()
GroupsGroupMarketCurrency.update_forward_refs()
GroupsGroupPhotos.update_forward_refs()
GroupsGroupPublicCategoryList.update_forward_refs()
GroupsGroupRole.update_forward_refs()
GroupsGroupSubject.update_forward_refs()
GroupsGroupSuggestedPrivacy.update_forward_refs()
GroupsGroupTag.update_forward_refs()
GroupsGroupTopics.update_forward_refs()
GroupsGroupType.update_forward_refs()
GroupsGroupVideo.update_forward_refs()
GroupsGroupWall.update_forward_refs()
GroupsGroupWiki.update_forward_refs()
GroupsGroupsArray.update_forward_refs()
GroupsLinksItem.update_forward_refs()
GroupsLiveCovers.update_forward_refs()
GroupsLongPollEvents.update_forward_refs()
GroupsLongPollServer.update_forward_refs()
GroupsLongPollSettings.update_forward_refs()
GroupsMarketInfo.update_forward_refs()
GroupsMarketState.update_forward_refs()
GroupsMemberRole.update_forward_refs()
GroupsMemberRolePermission.update_forward_refs()
GroupsMemberRoleStatus.update_forward_refs()
GroupsMemberStatus.update_forward_refs()
GroupsMemberStatusFull.update_forward_refs()
GroupsOnlineStatus.update_forward_refs()
GroupsOnlineStatusType.update_forward_refs()
GroupsOwnerXtrBanInfo.update_forward_refs()
GroupsOwnerXtrBanInfoType.update_forward_refs()
GroupsProfileItem.update_forward_refs()
GroupsRoleOptions.update_forward_refs()
GroupsSettingsTwitter.update_forward_refs()
GroupsSubjectItem.update_forward_refs()
GroupsTokenPermissionSetting.update_forward_refs()
GroupsUserXtrRole.update_forward_refs()
LikesType.update_forward_refs()
LinkTargetObject.update_forward_refs()
MarketCurrency.update_forward_refs()
MarketMarketAlbum.update_forward_refs()
MarketMarketCategory.update_forward_refs()
MarketMarketCategoryNested.update_forward_refs()
MarketMarketCategoryOld.update_forward_refs()
MarketMarketCategoryTree.update_forward_refs()
MarketMarketItem.update_forward_refs()
MarketMarketItemAvailability.update_forward_refs()
MarketMarketItemFull.update_forward_refs()
MarketOrder.update_forward_refs()
MarketOrderItem.update_forward_refs()
MarketPrice.update_forward_refs()
MarketSection.update_forward_refs()
MediaRestriction.update_forward_refs()
MessagesAudioMessage.update_forward_refs()
MessagesChat.update_forward_refs()
MessagesChatFull.update_forward_refs()
MessagesChatPreview.update_forward_refs()
MessagesChatPushSettings.update_forward_refs()
MessagesChatRestrictions.update_forward_refs()
MessagesChatSettings.update_forward_refs()
MessagesChatSettingsAcl.update_forward_refs()
MessagesChatSettingsPermissions.update_forward_refs()
MessagesChatSettingsPhoto.update_forward_refs()
MessagesChatSettingsState.update_forward_refs()
MessagesConversation.update_forward_refs()
MessagesConversationCanWrite.update_forward_refs()
MessagesConversationMember.update_forward_refs()
MessagesConversationPeer.update_forward_refs()
MessagesConversationPeerType.update_forward_refs()
MessagesConversationSortId.update_forward_refs()
MessagesConversationWithMessage.update_forward_refs()
MessagesForeignMessage.update_forward_refs()
MessagesForward.update_forward_refs()
MessagesGraffiti.update_forward_refs()
MessagesHistoryAttachment.update_forward_refs()
MessagesHistoryMessageAttachment.update_forward_refs()
MessagesHistoryMessageAttachmentType.update_forward_refs()
MessagesKeyboard.update_forward_refs()
MessagesKeyboardButton.update_forward_refs()
MessagesKeyboardButtonAction.update_forward_refs()
MessagesLastActivity.update_forward_refs()
MessagesLongpollMessages.update_forward_refs()
MessagesLongpollParams.update_forward_refs()
MessagesMessage.update_forward_refs()
MessagesMessageAction.update_forward_refs()
MessagesMessageActionPhoto.update_forward_refs()
MessagesMessageActionStatus.update_forward_refs()
MessagesMessageAttachment.update_forward_refs()
MessagesMessageAttachmentType.update_forward_refs()
MessagesMessageRequestData.update_forward_refs()
MessagesMessagesArray.update_forward_refs()
MessagesOutReadBy.update_forward_refs()
MessagesPinnedMessage.update_forward_refs()
MessagesPushSettings.update_forward_refs()
MessagesTemplateActionTypeNames.update_forward_refs()
MessagesUserXtrInvitedBy.update_forward_refs()
NewsfeedCommentsFilters.update_forward_refs()
NewsfeedEventActivity.update_forward_refs()
NewsfeedFilters.update_forward_refs()
NewsfeedIgnoreItemType.update_forward_refs()
NewsfeedItemAudio.update_forward_refs()
NewsfeedItemAudioAudio.update_forward_refs()
NewsfeedItemBase.update_forward_refs()
NewsfeedItemDigest.update_forward_refs()
NewsfeedItemDigestButton.update_forward_refs()
NewsfeedItemDigestFooter.update_forward_refs()
NewsfeedItemDigestFullItem.update_forward_refs()
NewsfeedItemDigestHeader.update_forward_refs()
NewsfeedItemDigestItem.update_forward_refs()
NewsfeedItemFriend.update_forward_refs()
NewsfeedItemFriendFriends.update_forward_refs()
NewsfeedItemHolidayRecommendationsBlockHeader.update_forward_refs()
NewsfeedItemPhoto.update_forward_refs()
NewsfeedItemPhotoPhotos.update_forward_refs()
NewsfeedItemPhotoTag.update_forward_refs()
NewsfeedItemPhotoTagPhotoTags.update_forward_refs()
NewsfeedItemPromoButton.update_forward_refs()
NewsfeedItemPromoButtonAction.update_forward_refs()
NewsfeedItemPromoButtonImage.update_forward_refs()
NewsfeedItemTopic.update_forward_refs()
NewsfeedItemVideo.update_forward_refs()
NewsfeedItemVideoVideo.update_forward_refs()
NewsfeedItemWallpost.update_forward_refs()
NewsfeedItemWallpostFeedback.update_forward_refs()
NewsfeedItemWallpostFeedbackAnswer.update_forward_refs()
NewsfeedItemWallpostFeedbackType.update_forward_refs()
NewsfeedItemWallpostType.update_forward_refs()
NewsfeedList.update_forward_refs()
NewsfeedListFull.update_forward_refs()
NewsfeedNewsfeedItem.update_forward_refs()
NewsfeedNewsfeedItemType.update_forward_refs()
NewsfeedNewsfeedPhoto.update_forward_refs()
NotesNote.update_forward_refs()
NotesNoteComment.update_forward_refs()
NotificationsFeedback.update_forward_refs()
NotificationsNotification.update_forward_refs()
NotificationsNotificationItem.update_forward_refs()
NotificationsNotificationParent.update_forward_refs()
NotificationsNotificationsComment.update_forward_refs()
NotificationsReply.update_forward_refs()
NotificationsSendMessageError.update_forward_refs()
NotificationsSendMessageItem.update_forward_refs()
OauthError.update_forward_refs()
OrdersAmount.update_forward_refs()
OrdersAmountItem.update_forward_refs()
OrdersOrder.update_forward_refs()
OrdersSubscription.update_forward_refs()
OwnerState.update_forward_refs()
PagesPrivacySettings.update_forward_refs()
PagesWikipage.update_forward_refs()
PagesWikipageFull.update_forward_refs()
PagesWikipageHistory.update_forward_refs()
PhotosCommentXtrPid.update_forward_refs()
PhotosImage.update_forward_refs()
PhotosImageType.update_forward_refs()
PhotosPhoto.update_forward_refs()
PhotosPhotoAlbum.update_forward_refs()
PhotosPhotoAlbumFull.update_forward_refs()
PhotosPhotoFalseable.update_forward_refs()
PhotosPhotoFull.update_forward_refs()
PhotosPhotoFullXtrRealOffset.update_forward_refs()
PhotosPhotoSizes.update_forward_refs()
PhotosPhotoSizesType.update_forward_refs()
PhotosPhotoTag.update_forward_refs()
PhotosPhotoUpload.update_forward_refs()
PhotosPhotoXtrRealOffset.update_forward_refs()
PhotosPhotoXtrTagInfo.update_forward_refs()
PhotosTagsSuggestionItem.update_forward_refs()
PhotosTagsSuggestionItemButton.update_forward_refs()
PodcastCover.update_forward_refs()
PodcastExternalData.update_forward_refs()
PollsAnswer.update_forward_refs()
PollsBackground.update_forward_refs()
PollsFriend.update_forward_refs()
PollsPoll.update_forward_refs()
PollsPollAnonymous.update_forward_refs()
PollsVoters.update_forward_refs()
PollsVotersUsers.update_forward_refs()
PrettyCardsPrettycard.update_forward_refs()
SearchHint.update_forward_refs()
SearchHintSection.update_forward_refs()
SearchHintType.update_forward_refs()
SecureLevel.update_forward_refs()
SecureSmsNotification.update_forward_refs()
SecureTokenChecked.update_forward_refs()
SecureTransaction.update_forward_refs()
StatsActivity.update_forward_refs()
StatsCity.update_forward_refs()
StatsCountry.update_forward_refs()
StatsPeriod.update_forward_refs()
StatsReach.update_forward_refs()
StatsSexAge.update_forward_refs()
StatsViews.update_forward_refs()
StatsWallpostStat.update_forward_refs()
StatusStatus.update_forward_refs()
StickersImageSet.update_forward_refs()
StorageValue.update_forward_refs()
StoreProduct.update_forward_refs()
StoreProductIcon.update_forward_refs()
StoreStickersKeyword.update_forward_refs()
StoreStickersKeywordSticker.update_forward_refs()
StoreStickersKeywordStickers.update_forward_refs()
StoriesClickableArea.update_forward_refs()
StoriesClickableSticker.update_forward_refs()
StoriesClickableStickers.update_forward_refs()
StoriesFeedItem.update_forward_refs()
StoriesPromoBlock.update_forward_refs()
StoriesReplies.update_forward_refs()
StoriesStatLine.update_forward_refs()
StoriesStory.update_forward_refs()
StoriesStoryLink.update_forward_refs()
StoriesStoryStats.update_forward_refs()
StoriesStoryStatsStat.update_forward_refs()
StoriesStoryStatsState.update_forward_refs()
StoriesStoryType.update_forward_refs()
StoriesUploadLinkText.update_forward_refs()
StoriesViewersItem.update_forward_refs()
UsersCareer.update_forward_refs()
UsersExports.update_forward_refs()
UsersFields.update_forward_refs()
UsersLastSeen.update_forward_refs()
UsersMilitary.update_forward_refs()
UsersOccupation.update_forward_refs()
UsersOnlineInfo.update_forward_refs()
UsersPersonal.update_forward_refs()
UsersRelative.update_forward_refs()
UsersSchool.update_forward_refs()
UsersSubscriptionsItem.update_forward_refs()
UsersUniversity.update_forward_refs()
UsersUser.update_forward_refs()
UsersUserConnections.update_forward_refs()
UsersUserCounters.update_forward_refs()
UsersUserFull.update_forward_refs()
UsersUserMin.update_forward_refs()
UsersUserRelation.update_forward_refs()
UsersUserSettingsXtr.update_forward_refs()
UsersUserType.update_forward_refs()
UsersUserXtrCounters.update_forward_refs()
UsersUserXtrType.update_forward_refs()
UsersUsersArray.update_forward_refs()
UtilsDomainResolved.update_forward_refs()
UtilsDomainResolvedType.update_forward_refs()
UtilsLastShortenedLink.update_forward_refs()
UtilsLinkChecked.update_forward_refs()
UtilsLinkCheckedStatus.update_forward_refs()
UtilsLinkStats.update_forward_refs()
UtilsLinkStatsExtended.update_forward_refs()
UtilsShortLink.update_forward_refs()
UtilsStats.update_forward_refs()
UtilsStatsCity.update_forward_refs()
UtilsStatsCountry.update_forward_refs()
UtilsStatsExtended.update_forward_refs()
UtilsStatsSexAge.update_forward_refs()
VideoLiveInfo.update_forward_refs()
VideoLiveSettings.update_forward_refs()
VideoRestrictionButton.update_forward_refs()
VideoSaveResult.update_forward_refs()
VideoVideo.update_forward_refs()
VideoVideoAlbumFull.update_forward_refs()
VideoVideoFiles.update_forward_refs()
VideoVideoFull.update_forward_refs()
VideoVideoImage.update_forward_refs()
WallAppPost.update_forward_refs()
WallAttachedNote.update_forward_refs()
WallCarouselBase.update_forward_refs()
WallCommentAttachment.update_forward_refs()
WallCommentAttachmentType.update_forward_refs()
WallGeo.update_forward_refs()
WallGraffiti.update_forward_refs()
WallPostCopyright.update_forward_refs()
WallPostSource.update_forward_refs()
WallPostSourceType.update_forward_refs()
WallPostType.update_forward_refs()
WallPostedPhoto.update_forward_refs()
WallViews.update_forward_refs()
WallWallComment.update_forward_refs()
WallWallCommentDonut.update_forward_refs()
WallWallCommentDonutPlaceholder.update_forward_refs()
WallWallpost.update_forward_refs()
WallWallpostAttachment.update_forward_refs()
WallWallpostAttachmentType.update_forward_refs()
WallWallpostCommentsDonut.update_forward_refs()
WallWallpostCommentsDonutPlaceholder.update_forward_refs()
WallWallpostDonut.update_forward_refs()
WallWallpostDonutPlaceholder.update_forward_refs()
WallWallpostFull.update_forward_refs()
WallWallpostToId.update_forward_refs()
WidgetsCommentMedia.update_forward_refs()
WidgetsCommentMediaType.update_forward_refs()
WidgetsCommentReplies.update_forward_refs()
WidgetsCommentRepliesItem.update_forward_refs()
WidgetsWidgetComment.update_forward_refs()
WidgetsWidgetLikes.update_forward_refs()
WidgetsWidgetPage.update_forward_refs()