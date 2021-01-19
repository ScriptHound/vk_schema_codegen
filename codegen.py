

class AccountAccountCounters:
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
	menu_clips_badge - No description
	messages - New messages number
	memories - New memories number
	notes - New notes number
	notifications - New notifications number
	photos - New photo tags number
	sdk - New sdk number
	"""
	app_requests = None
	events = None
	faves = None
	friends = None
	friends_suggestions = None
	friends_recommendations = None
	gifts = None
	groups = None
	menu_discover_badge = None
	menu_clips_badge = None
	messages = None
	memories = None
	notes = None
	notifications = None
	photos = None
	sdk = None


class AccountInfo:
	"""VK Object AccountInfo

	wishlists_ae_promo_banner_show - No description
	2fa_required - Two factor authentication is enabled
	country - Country code
	https_required - Information whether HTTPS-only is enabled
	intro - Information whether user has been processed intro
	show_vk_apps_intro - No description
	mini_apps_ads_slot_id - Ads slot id for MyTarget
	qr_promotion - No description
	link_redirects - No description
	lang - Language ID
	no_wall_replies - Information whether wall comments should be hidden
	own_posts_default - Information whether only owners posts should be shown
	subscriptions - No description
	"""
	wishlists_ae_promo_banner_show = None
	_2fa_required = None
	country = None
	https_required = None
	intro = None
	show_vk_apps_intro = None
	mini_apps_ads_slot_id = None
	qr_promotion = None
	link_redirects = None
	lang = None
	no_wall_replies = None
	own_posts_default = None
	subscriptions = None


class AccountNAmeRequest:
	"""VK Object AccountNAmeRequest

	first_name - First name in request
	id - Request ID needed to cancel the request
	last_name - Last name in request
	status - No description
	lang - Text to display to user
	link_href - href for link in lang field
	link_label - label to display for link in lang field
	"""
	first_name = None
	id = None
	last_name = None
	status = None
	lang = None
	link_href = None
	link_label = None


class AccountNAmeRequestStAtus:
	"""VK Object AccountNAmeRequestStAtus

	success - None
	processing - None
	declined - None
	was_accepted - None
	was_declined - None
	declined_with_link - None
	response - None
	response_with_link - None
	"""
	success = 0
	processing = 1
	declined = 2
	was_accepted = 3
	was_declined = 4
	declined_with_link = 5
	response = 6
	response_with_link = 7


class AccountOffer:
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
	description = None
	id = None
	img = None
	instruction = None
	instruction_html = None
	price = None
	short_description = None
	tag = None
	title = None
	currency_amount = None
	link_id = None
	link_type = None


class AccountPushConversAtions:
	"""VK Object AccountPushConversAtions

	count - Items count
	items - No description
	"""
	count = None
	items = None


class AccountPushConversAtionsItem:
	"""VK Object AccountPushConversAtionsItem

	disabled_until - Time until that notifications are disabled in seconds
	peer_id - Peer ID
	sound - Information whether the sound are enabled
	"""
	disabled_until = None
	peer_id = None
	sound = None


class AccountPushPArAms:
	"""VK Object AccountPushPArAms

	msg - No description
	chat - No description
	like - No description
	repost - No description
	comment - No description
	mention - No description
	reply - No description
	new_post - No description
	wall_post - No description
	wall_publish - No description
	friend - No description
	friend_found - No description
	friend_accepted - No description
	group_invite - No description
	group_accepted - No description
	birthday - No description
	event_soon - No description
	app_request - No description
	sdk_open - No description
	"""
	msg = None
	chat = None
	like = None
	repost = None
	comment = None
	mention = None
	reply = None
	new_post = None
	wall_post = None
	wall_publish = None
	friend = None
	friend_found = None
	friend_accepted = None
	group_invite = None
	group_accepted = None
	birthday = None
	event_soon = None
	app_request = None
	sdk_open = None


class AccountPushPArAmsMode:
	"""VK Object AccountPushPArAmsMode

	on - None
	off - None
	no_sound - None
	no_text - None
	"""
	on = 0
	off = 1
	no_sound = 2
	no_text = 3


class AccountPushPArAmsOnoff:
	"""VK Object AccountPushPArAmsOnoff

	on - None
	off - None
	"""
	on = 0
	off = 1


class AccountPushPArAmsSettings:
	"""VK Object AccountPushPArAmsSettings

	on - None
	off - None
	fr_of_fr - None
	"""
	on = 0
	off = 1
	fr_of_fr = 2


class AccountPushSettings:
	"""VK Object AccountPushSettings

	disabled - Information whether notifications are disabled
	disabled_until - Time until that notifications are disabled in Unixtime
	settings - No description
	conversations - No description
	"""
	disabled = None
	disabled_until = None
	settings = None
	conversations = None


class AccountUserSettings:
	"""VK Object AccountUserSettings

	photo_200 - URL of square photo of the user with 200 pixels in width
	is_service_account - flag about service account
	"""
	photo_200 = <built-in function iter>
	is_service_account = <built-in function iter>


class AccountUserSettingsInterest:
	"""VK Object AccountUserSettingsInterest

	title - No description
	value - No description
	"""
	title = None
	value = None


class AccountUserSettingsInterests:
	"""VK Object AccountUserSettingsInterests

	activities - No description
	interests - No description
	music - No description
	tv - No description
	movies - No description
	books - No description
	games - No description
	quotes - No description
	about - No description
	"""
	activities = None
	interests = None
	music = None
	tv = None
	movies = None
	books = None
	games = None
	quotes = None
	about = None


class AddressesFields:
	"""VK Object AddressesFields

	id - None
	title - None
	address - None
	additional_address - None
	country_id - None
	city_id - None
	metro_station_id - None
	latitude - None
	longitude - None
	distance - None
	work_info_status - None
	timetable - None
	phone - None
	time_offset - None
	"""
	id = 0
	title = 1
	address = 2
	additional_address = 3
	country_id = 4
	city_id = 5
	metro_station_id = 6
	latitude = 7
	longitude = 8
	distance = 9
	work_info_status = 10
	timetable = 11
	phone = 12
	time_offset = 13


class AdsAccessRole:
	"""VK Object AdsAccessRole

	admin - None
	manager - None
	reports - None
	"""
	admin = 0
	manager = 1
	reports = 2


class AdsAccessRolePublic:
	"""VK Object AdsAccessRolePublic

	manager - None
	reports - None
	"""
	manager = 0
	reports = 1


class AdsAccesses:
	"""VK Object AdsAccesses

	client_id - Client ID
	role - No description
	"""
	client_id = None
	role = None


class AdsAccount:
	"""VK Object AdsAccount

	access_role - No description
	account_id - Account ID
	account_status - Information whether account is active
	account_type - No description
	account_name - Account name
	can_view_budget - Can user view account budget
	"""
	access_role = None
	account_id = None
	account_status = None
	account_type = None
	account_name = None
	can_view_budget = None


class AdsAccountType:
	"""VK Object AdsAccountType

	general - None
	agency - None
	"""
	general = 0
	agency = 1


class AdsAd:
	"""VK Object AdsAd

	ad_format - Ad format
	ad_platform - Ad platform
	all_limit - Total limit
	approved - No description
	campaign_id - Campaign ID
	category1_id - Category ID
	category2_id - Additional category ID
	cost_type - No description
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
	status - No description
	video - Information whether the ad is a video
	"""
	ad_format = None
	ad_platform = None
	all_limit = None
	approved = None
	campaign_id = None
	category1_id = None
	category2_id = None
	cost_type = None
	cpc = None
	cpm = None
	cpa = None
	ocpm = None
	autobidding_max_cost = None
	disclaimer_medical = None
	disclaimer_specialist = None
	disclaimer_supplements = None
	id = None
	impressions_limit = None
	impressions_limited = None
	name = None
	status = None
	video = None
NoneNone

class AdsAdLAyout:
	"""VK Object AdsAdLAyout

	ad_format - Ad format
	campaign_id - Campaign ID
	cost_type - No description
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
	ad_format = None
	campaign_id = None
	cost_type = None
	description = None
	id = None
	image_src = None
	image_src_2x = None
	link_domain = None
	link_url = None
	preview_link = None
	title = None
	video = None
None

class AdsCAmpAign:
	"""VK Object AdsCAmpAign

	all_limit - Campaign's total limit, rubles
	day_limit - Campaign's day limit, rubles
	id - Campaign ID
	name - Campaign title
	start_time - Campaign start time, as Unixtime
	status - No description
	stop_time - Campaign stop time, as Unixtime
	type - No description
	"""
	all_limit = None
	day_limit = None
	id = None
	name = None
	start_time = None
	status = None
	stop_time = None
	type = None
None

class AdsCAmpAignType:
	"""VK Object AdsCAmpAignType

	normal - None
	vk_apps_managed - None
	mobile_apps - None
	promoted_posts - None
	"""
	normal = 0
	vk_apps_managed = 1
	mobile_apps = 2
	promoted_posts = 3


class AdsCAtegory:
	"""VK Object AdsCAtegory

	id - Category ID
	name - Category name
	subcategories - No description
	"""
	id = None
	name = None
	subcategories = None


class AdsClient:
	"""VK Object AdsClient

	all_limit - Client's total limit, rubles
	day_limit - Client's day limit, rubles
	id - Client ID
	name - Client name
	"""
	all_limit = None
	day_limit = None
	id = None
	name = None


class AdsCriteriA:
	"""VK Object AdsCriteriA

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
	sex - No description
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
	age_from = None
	age_to = None
	apps = None
	apps_not = None
	birthday = None
	cities = None
	cities_not = None
	country = None
	districts = None
	groups = None
	interest_categories = None
	interests = None
	paying = None
	positions = None
	religions = None
	retargeting_groups = None
	retargeting_groups_not = None
	school_from = None
	school_to = None
	schools = None
	sex = None
	stations = None
	statuses = None
	streets = None
	travellers = None
	uni_from = None
	uni_to = None
	user_browsers = None
	user_devices = None
	user_os = None
None

class AdsDemoStAts:
	"""VK Object AdsDemoStAts

	id - Object ID
	stats - No description
	type - No description
	"""
	id = None
	stats = None
	type = None


class AdsDemostAtsFormAt:
	"""VK Object AdsDemostAtsFormAt

	age - No description
	cities - No description
	day - Day as YYYY-MM-DD
	month - Month as YYYY-MM
	overall - 1 if period=overall
	sex - No description
	sex_age - No description
	"""
	age = None
	cities = None
	day = None
	month = None
	overall = None
	sex = None
	sex_age = None


class AdsFloodStAts:
	"""VK Object AdsFloodStAts

	left - Requests left
	refresh - Time to refresh in seconds
	"""
	left = None
	refresh = None


class AdsLinkStAtus:
	"""VK Object AdsLinkStAtus

	description - Reject reason
	redirect_url - URL
	status - Link status
	"""
	description = None
	redirect_url = None
	status = None


class AdsLookAlikeRequest:
	"""VK Object AdsLookAlikeRequest

	id - Lookalike request ID
	create_time - Lookalike request create time, as Unixtime
	update_time - Lookalike request update time, as Unixtime
	scheduled_delete_time - Time by which lookalike request would be deleted, as Unixtime
	status - Lookalike request status
	source_type - Lookalike request source type
	source_retargeting_group_id - Retargeting group id, which was used as lookalike seed
	source_name - Lookalike request seed name (retargeting group name)
	audience_count - Lookalike request seed audience size
	save_audience_levels - No description
	"""
	id = None
	create_time = None
	update_time = None
	scheduled_delete_time = None
	status = None
	source_type = None
	source_retargeting_group_id = None
	source_name = None
	audience_count = None
	save_audience_levels = None


class AdsLookAlikeRequestSAveAudienceLevel:
	"""VK Object AdsLookAlikeRequestSAveAudienceLevel

	level - Save audience level id, which is used in save audience queries
	audience_count - Saved audience audience size for according level
	"""
	level = None
	audience_count = None


class AdsMusiciAn:
	"""VK Object AdsMusiciAn

	id - Targeting music artist ID
	name - Music artist name
	avatar - Music artist photo
	"""
	id = None
	name = None
	avatar = None


class AdsObjectType:
	"""VK Object AdsObjectType

	ad - None
	campaign - None
	client - None
	office - None
	"""
	ad = 0
	campaign = 1
	client = 2
	office = 3


class AdsPArAgrAphs:
	"""VK Object AdsPArAgrAphs

	paragraph - Rules paragraph
	"""
	paragraph = None


class AdsPromotedPostReAch:
	"""VK Object AdsPromotedPostReAch

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
	hide = None
	id = None
	join_group = None
	links = None
	reach_subscribers = None
	reach_total = None
	report = None
	to_group = None
	unsubscribe = None
	video_views_100p = None
	video_views_25p = None
	video_views_3s = None
	video_views_50p = None
	video_views_75p = None
	video_views_start = None


class AdsRejectReAson:
	"""VK Object AdsRejectReAson

	comment - Comment text
	rules - No description
	"""
	comment = None
	rules = None


class AdsRules:
	"""VK Object AdsRules

	paragraphs - No description
	title - Comment
	"""
	paragraphs = None
	title = None


class AdsStAts:
	"""VK Object AdsStAts

	id - Object ID
	stats - No description
	type - No description
	views_times - No description
	"""
	id = None
	stats = None
	type = None
	views_times = None


class AdsStAtsAge:
	"""VK Object AdsStAtsAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Age interval
	"""
	clicks_rate = None
	impressions_rate = None
	value = None


class AdsStAtsCities:
	"""VK Object AdsStAtsCities

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	name - City name
	value - City ID
	"""
	clicks_rate = None
	impressions_rate = None
	name = None
	value = None


class AdsStAtsFormAt:
	"""VK Object AdsStAtsFormAt

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
	clicks = None
	day = None
	impressions = None
	join_rate = None
	month = None
	overall = None
	reach = None
	spent = None
	video_clicks_site = None
	video_views = None
	video_views_full = None
	video_views_half = None


class AdsStAtsSex:
	"""VK Object AdsStAtsSex

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - No description
	"""
	clicks_rate = None
	impressions_rate = None
	value = None


class AdsStAtsSexAge:
	"""VK Object AdsStAtsSexAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Sex and age interval
	"""
	clicks_rate = None
	impressions_rate = None
	value = None


class AdsStAtsSexVAlue:
	"""VK Object AdsStAtsSexVAlue

	f - None
	m - None
	"""
	f = 0
	m = 1


class AdsStAtsViewsTimes:
	"""VK Object AdsStAtsViewsTimes

	views_ads_times_1 - No description
	views_ads_times_2 - No description
	views_ads_times_3 - No description
	views_ads_times_4 - No description
	views_ads_times_5 - No description
	views_ads_times_6 - No description
	views_ads_times_7 - No description
	views_ads_times_8 - No description
	views_ads_times_9 - No description
	views_ads_times_10 - No description
	views_ads_times_11_plus - No description
	"""
	views_ads_times_1 = None
	views_ads_times_2 = None
	views_ads_times_3 = None
	views_ads_times_4 = None
	views_ads_times_5 = None
	views_ads_times_6 = None
	views_ads_times_7 = None
	views_ads_times_8 = None
	views_ads_times_9 = None
	views_ads_times_10 = None
	views_ads_times_11_plus = None


class AdsTArgSettings:
	"""VK Object AdsTArgSettings

	id - Ad ID
	campaign_id - Campaign ID
	"""
	id = <built-in function iter>
	campaign_id = <built-in function iter>


class AdsTArgStAts:
	"""VK Object AdsTArgStAts

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
	audience_count = None
	recommended_cpc = None
	recommended_cpm = None
	recommended_cpc_50 = None
	recommended_cpm_50 = None
	recommended_cpc_70 = None
	recommended_cpm_70 = None
	recommended_cpc_90 = None
	recommended_cpm_90 = None


class AdsTArgSuggestions:
	"""VK Object AdsTArgSuggestions

	id - Object ID
	name - Object name
	"""
	id = None
	name = None


class AdsTArgSuggestionsCities:
	"""VK Object AdsTArgSuggestionsCities

	id - Object ID
	name - Object name
	parent - Parent object
	"""
	id = None
	name = None
	parent = None


class AdsTArgSuggestionsRegions:
	"""VK Object AdsTArgSuggestionsRegions

	id - Object ID
	name - Object name
	type - Object type
	"""
	id = None
	name = None
	type = None


class AdsTArgSuggestionsSchools:
	"""VK Object AdsTArgSuggestionsSchools

	desc - Full school title
	id - School ID
	name - School title
	parent - City name
	type - No description
	"""
	desc = None
	id = None
	name = None
	parent = None
	type = None


class AdsTArgSuggestionsSchoolsType:
	"""VK Object AdsTArgSuggestionsSchoolsType

	school - None
	university - None
	faculty - None
	chair - None
	"""
	school = 0
	university = 1
	faculty = 2
	chair = 3


class AdsTArgetGroup:
	"""VK Object AdsTArgetGroup

	audience_count - Audience
	domain - Site domain
	id - Group ID
	lifetime - Number of days for user to be in group
	name - Group name
	pixel - Pixel code
	"""
	audience_count = None
	domain = None
	id = None
	lifetime = None
	name = None
	pixel = None


class AdsUpdAteOfficeUsersResult:
	"""VK Object AdsUpdAteOfficeUsersResult

	user_id - No description
	is_success - No description
	error - No description
	"""
	user_id = None
	is_success = None
	error = None


class AdsUserSpecificAtion:
	"""VK Object AdsUserSpecificAtion

	user_id - No description
	role - No description
	grant_access_to_all_clients - No description
	client_ids - No description
	view_budget - No description
	"""
	user_id = None
	role = None
	grant_access_to_all_clients = None
	client_ids = None
	view_budget = None


class AdsUserSpecificAtionCutted:
	"""VK Object AdsUserSpecificAtionCutted

	user_id - No description
	role - No description
	client_id - No description
	view_budget - No description
	"""
	user_id = None
	role = None
	client_id = None
	view_budget = None


class AdsUsers:
	"""VK Object AdsUsers

	accesses - No description
	user_id - User ID
	"""
	accesses = None
	user_id = None


class AdswebGetAdCAtegoriesResponseCAtegoriesCAtegory:
	"""VK Object AdswebGetAdCAtegoriesResponseCAtegoriesCAtegory

	id - No description
	name - No description
	"""
	id = None
	name = None


class AdswebGetAdUnitsResponseAdUnitsAdUnit:
	"""VK Object AdswebGetAdUnitsResponseAdUnitsAdUnit

	id - No description
	site_id - No description
	name - No description
	"""
	id = None
	site_id = None
	name = None


class AdswebGetFrAudHistoryResponseEntriesEntry:
	"""VK Object AdswebGetFrAudHistoryResponseEntriesEntry

	site_id - No description
	day - No description
	"""
	site_id = None
	day = None


class AdswebGetSitesResponseSitesSite:
	"""VK Object AdswebGetSitesResponseSitesSite

	id - No description
	status_user - No description
	status_moder - No description
	domains - No description
	"""
	id = None
	status_user = None
	status_moder = None
	domains = None


class AdswebGetStAtisticsResponseItemsItem:
	"""VK Object AdswebGetStAtisticsResponseItemsItem

	site_id - No description
	ad_unit_id - No description
	overall_count - No description
	months_count - No description
	month_min - No description
	month_max - No description
	days_count - No description
	day_min - No description
	day_max - No description
	hours_count - No description
	hour_min - No description
	hour_max - No description
	"""
	site_id = None
	ad_unit_id = None
	overall_count = None
	months_count = None
	month_min = None
	month_max = None
	days_count = None
	day_min = None
	day_max = None
	hours_count = None
	hour_min = None
	hour_max = None


class AppWidgetsPhoto:
	"""VK Object AppWidgetsPhoto

	id - Image ID
	images - No description
	"""
	id = None
	images = None


class AppWidgetsPhotos:
	"""VK Object AppWidgetsPhotos

	count - No description
	items - No description
	"""
	count = None
	items = None


class AppsApp:
	"""VK Object AppsApp

	author_url - Application author's URL
	banner_1120 - URL of the app banner with 1120 px in width
	banner_560 - URL of the app banner with 560 px in width
	icon_16 - URL of the app icon with 16 px in width
	is_new - Is new flag
	push_enabled - Is push enabled
	screen_orientation - Screen orientation
	friends - No description
	catalog_position - Catalog position
	description - Application description
	genre - Genre name
	genre_id - Genre ID
	international - Information whether the application is multilanguage
	is_in_catalog - Information whether application is in mobile catalog
	leaderboard_type - No description
	members_count - Members number
	platform_id - Application ID in store
	published_date - Date when the application has been published in Unixtime
	screen_name - Screen name
	section - Application section name
	"""
	author_url = <built-in function iter>
	banner_1120 = <built-in function iter>
	banner_560 = <built-in function iter>
	icon_16 = <built-in function iter>
	is_new = <built-in function iter>
	push_enabled = <built-in function iter>
	screen_orientation = <built-in function iter>
	friends = <built-in function iter>
	catalog_position = <built-in function iter>
	description = <built-in function iter>
	genre = <built-in function iter>
	genre_id = <built-in function iter>
	international = <built-in function iter>
	is_in_catalog = <built-in function iter>
	leaderboard_type = <built-in function iter>
	members_count = <built-in function iter>
	platform_id = <built-in function iter>
	published_date = <built-in function iter>
	screen_name = <built-in function iter>
	section = <built-in function iter>
None

class AppsAppMin:
	"""VK Object AppsAppMin

	type - No description
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
	type = None
	id = None
	title = None
	author_owner_id = None
	is_installed = None
	icon_139 = None
	icon_150 = None
	icon_278 = None
	icon_576 = None
	background_loader_color = None
	loader_icon = None
	icon_75 = None


class AppsAppType:
	"""VK Object AppsAppType

	app - None
	game - None
	site - None
	standalone - None
	vk_app - None
	community_app - None
	html5_game - None
	mini_app - None
	"""
	app = 0
	game = 1
	site = 2
	standalone = 3
	vk_app = 4
	community_app = 5
	html5_game = 6
	mini_app = 7


class AppsLeAderboArd:
	"""VK Object AppsLeAderboArd

	level - Level
	points - Points number
	score - Score number
	user_id - User ID
	"""
	level = None
	points = None
	score = None
	user_id = None


class AppsScope:
	"""VK Object AppsScope

	name - Scope name
	title - Scope title
	"""
	name = None
	title = None


class AudioAudio:
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
	access_key = None
	artist = None
	id = None
	owner_id = None
	title = None
	url = None
	duration = None
	date = None
	album_id = None
	genre_id = None
	performer = None
None

class BaseCity:
	"""VK Object BaseCity

	id - City ID
	title - City title
	"""
	id = None
	title = None


class BaseCommentsInfo:
	"""VK Object BaseCommentsInfo

	can_post - Information whether current user can comment the post
	count - Comments number
	groups_can_post - Information whether groups can comment the post
	donut - No description
	"""
	can_post = None
	count = None
	groups_can_post = None
	donut = None


class BaseCountry:
	"""VK Object BaseCountry

	id - Country ID
	title - Country title
	"""
	id = None
	title = None


class BaseCropPhoto:
	"""VK Object BaseCropPhoto

	photo - No description
	crop - No description
	rect - No description
	"""
	photo = None
	crop = None
	rect = None


class BaseCropPhotoCrop:
	"""VK Object BaseCropPhotoCrop

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x = None
	y = None
	x2 = None
	y2 = None


class BaseCropPhotoRect:
	"""VK Object BaseCropPhotoRect

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x = None
	y = None
	x2 = None
	y2 = None


class BaseError:
	"""VK Object BaseError

	error_code - Error code
	error_subcode - Error subcode
	error_msg - Error message
	error_text - Localized error message
	request_params - No description
	"""
	error_code = None
	error_subcode = None
	error_msg = None
	error_text = None
	request_params = None


class BaseGeo:
	"""VK Object BaseGeo

	coordinates - No description
	place - No description
	showmap - Information whether a map is showed
	type - Place type
	"""
	coordinates = None
	place = None
	showmap = None
	type = None


class BaseGeoCoordinates:
	"""VK Object BaseGeoCoordinates

	latitude - No description
	longitude - No description
	"""
	latitude = None
	longitude = None


class BaseGradientPoint:
	"""VK Object BaseGradientPoint

	color - Hex color code without #
	position - Point position
	"""
	color = None
	position = None


class BaseImage:
	"""VK Object BaseImage

	id - No description
	height - Image height
	url - Image url
	width - Image width
	"""
	id = None
	height = None
	url = None
	width = None


class BaseLikes:
	"""VK Object BaseLikes

	count - Likes number
	user_likes - Information whether current user likes the photo
	"""
	count = None
	user_likes = None


class BaseLikesInfo:
	"""VK Object BaseLikesInfo

	can_like - Information whether current user can like the post
	can_publish - Information whether current user can repost
	count - Likes number
	user_likes - Information whether current uer has liked the post
	"""
	can_like = None
	can_publish = None
	count = None
	user_likes = None


class BaseLink:
	"""VK Object BaseLink

	application - No description
	button - No description
	caption - Link caption
	description - Link description
	id - Link ID
	is_favorite - No description
	photo - No description
	preview_page - String ID of the page with article preview
	preview_url - URL of the page with article preview
	product - No description
	rating - No description
	title - Link title
	url - Link URL
	target_object - No description
	is_external - Information whether the current link is external
	video - Video from link
	"""
	application = None
	button = None
	caption = None
	description = None
	id = None
	is_favorite = None
	photo = None
	preview_page = None
	preview_url = None
	product = None
	rating = None
	title = None
	url = None
	target_object = None
	is_external = None
	video = None


class BaseLinkApplication:
	"""VK Object BaseLinkApplication

	app_id - Application Id
	store - No description
	"""
	app_id = None
	store = None


class BaseLinkApplicationStore:
	"""VK Object BaseLinkApplicationStore

	id - Store Id
	name - Store name
	"""
	id = None
	name = None


class BaseLinkButton:
	"""VK Object BaseLinkButton

	action - Button action
	title - Button title
	block_id - Target block id
	section_id - Target section id
	curator_id - curator id
	owner_id - Owner id
	icon - Button icon name, e.g. 'phone' or 'gift'
	style - No description
	"""
	action = None
	title = None
	block_id = None
	section_id = None
	curator_id = None
	owner_id = None
	icon = None
	style = None


class BaseLinkButtonAction:
	"""VK Object BaseLinkButtonAction

	type - No description
	url - Action URL
	consume_reason - No description
	"""
	type = None
	url = None
	consume_reason = None


class BaseLinkButtonActionType:
	"""VK Object BaseLinkButtonActionType

	open_url - None
	"""
	open_url = 0


class BaseLinkButtonStyle:
	"""VK Object BaseLinkButtonStyle

	primary - None
	secondary - None
	"""
	primary = 0
	secondary = 1


class BaseLinkProduct:
	"""VK Object BaseLinkProduct

	price - No description
	merchant - No description
	orders_count - No description
	"""
	price = None
	merchant = None
	orders_count = None


class BaseLinkProductStatus:
	"""VK Object BaseLinkProductStatus

	active - None
	blocked - None
	sold - None
	deleted - None
	archived - None
	"""
	active = 0
	blocked = 1
	sold = 2
	deleted = 3
	archived = 4


class BaseLinkRating:
	"""VK Object BaseLinkRating

	reviews_count - Count of reviews
	stars - Count of stars
	"""
	reviews_count = None
	stars = None


class BaseMessageError:
	"""VK Object BaseMessageError

	code - Error code
	description - Error message
	"""
	code = None
	description = None


class BaseOBject:
	"""VK Object BaseOBject

	id - Object ID
	title - Object title
	"""
	id = None
	title = None


class BaseOBjectCount:
	"""VK Object BaseOBjectCount

	count - Items count
	"""
	count = None


class BaseOBjectWithName:
	"""VK Object BaseOBjectWithName

	id - Object ID
	name - Object name
	"""
	id = None
	name = None


class BasePlace:
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
	address = None
	checkins = None
	city = None
	country = None
	created = None
	icon = None
	id = None
	latitude = None
	longitude = None
	title = None
	type = None
None

class BaseRepostsInfo:
	"""VK Object BaseRepostsInfo

	count - Total reposts counter. Sum of wall and mail reposts counters
	wall_count - Wall reposts counter
	mail_count - Mail reposts counter
	user_reposted - Information whether current user has reposted the post
	"""
	count = None
	wall_count = None
	mail_count = None
	user_reposted = None


class BaseRequestParam:
	"""VK Object BaseRequestParam

	key - Parameter name
	value - Parameter value
	"""
	key = None
	value = None
None

class BaseSticker:
	"""VK Object BaseSticker

	sticker_id - Sticker ID
	product_id - Pack ID
	images - No description
	images_with_background - No description
	animation_url - URL of sticker animation script
	animations - Array of sticker animation script objects
	is_allowed - Information whether the sticker is allowed
	"""
	sticker_id = None
	product_id = None
	images = None
	images_with_background = None
	animation_url = None
	animations = None
	is_allowed = None


class BaseStickerAnimation:
	"""VK Object BaseStickerAnimation

	type - Type of animation script
	url - URL of animation script
	"""
	type = None
	url = None
None

class BaseUploadServer:
	"""VK Object BaseUploadServer

	upload_url - Upload URL
	"""
	upload_url = None


class BaseUserGroupFields:
	"""VK Object BaseUserGroupFields

	about - None
	action_button - None
	activities - None
	activity - None
	addresses - None
	admin_level - None
	age_limits - None
	author_id - None
	ban_info - None
	bdate - None
	blacklisted - None
	blacklisted_by_me - None
	books - None
	can_create_topic - None
	can_message - None
	can_post - None
	can_see_all_posts - None
	can_see_audio - None
	can_send_friend_request - None
	can_upload_video - None
	can_write_private_message - None
	career - None
	city - None
	common_count - None
	connections - None
	contacts - None
	counters - None
	country - None
	cover - None
	crop_photo - None
	deactivated - None
	description - None
	domain - None
	education - None
	exports - None
	finish_date - None
	fixed_post - None
	followers_count - None
	friend_status - None
	games - None
	has_market_app - None
	has_mobile - None
	has_photo - None
	home_town - None
	id - None
	interests - None
	is_admin - None
	is_closed - None
	is_favorite - None
	is_friend - None
	is_hidden_from_feed - None
	is_member - None
	is_messages_blocked - None
	can_send_notify - None
	is_subscribed - None
	last_seen - None
	links - None
	lists - None
	maiden_name - None
	main_album_id - None
	main_section - None
	market - None
	member_status - None
	members_count - None
	military - None
	movies - None
	music - None
	name - None
	nickname - None
	occupation - None
	online - None
	online_status - None
	personal - None
	phone - None
	photo_100 - None
	photo_200 - None
	photo_200_orig - None
	photo_400_orig - None
	photo_50 - None
	photo_id - None
	photo_max - None
	photo_max_orig - None
	quotes - None
	relation - None
	relatives - None
	schools - None
	screen_name - None
	sex - None
	site - None
	start_date - None
	status - None
	timezone - None
	trending - None
	tv - None
	type - None
	universities - None
	verified - None
	wall_comments - None
	wiki_page - None
	vk_admin_status - None
	"""
	about = 0
	action_button = 1
	activities = 2
	activity = 3
	addresses = 4
	admin_level = 5
	age_limits = 6
	author_id = 7
	ban_info = 8
	bdate = 9
	blacklisted = 10
	blacklisted_by_me = 11
	books = 12
	can_create_topic = 13
	can_message = 14
	can_post = 15
	can_see_all_posts = 16
	can_see_audio = 17
	can_send_friend_request = 18
	can_upload_video = 19
	can_write_private_message = 20
	career = 21
	city = 22
	common_count = 23
	connections = 24
	contacts = 25
	counters = 26
	country = 27
	cover = 28
	crop_photo = 29
	deactivated = 30
	description = 31
	domain = 32
	education = 33
	exports = 34
	finish_date = 35
	fixed_post = 36
	followers_count = 37
	friend_status = 38
	games = 39
	has_market_app = 40
	has_mobile = 41
	has_photo = 42
	home_town = 43
	id = 44
	interests = 45
	is_admin = 46
	is_closed = 47
	is_favorite = 48
	is_friend = 49
	is_hidden_from_feed = 50
	is_member = 51
	is_messages_blocked = 52
	can_send_notify = 53
	is_subscribed = 54
	last_seen = 55
	links = 56
	lists = 57
	maiden_name = 58
	main_album_id = 59
	main_section = 60
	market = 61
	member_status = 62
	members_count = 63
	military = 64
	movies = 65
	music = 66
	name = 67
	nickname = 68
	occupation = 69
	online = 70
	online_status = 71
	personal = 72
	phone = 73
	photo_100 = 74
	photo_200 = 75
	photo_200_orig = 76
	photo_400_orig = 77
	photo_50 = 78
	photo_id = 79
	photo_max = 80
	photo_max_orig = 81
	quotes = 82
	relation = 83
	relatives = 84
	schools = 85
	screen_name = 86
	sex = 87
	site = 88
	start_date = 89
	status = 90
	timezone = 91
	trending = 92
	tv = 93
	type = 94
	universities = 95
	verified = 96
	wall_comments = 97
	wiki_page = 98
	vk_admin_status = 99


class BaseUserId:
	"""VK Object BaseUserId

	user_id - User ID
	"""
	user_id = None
None

class BoardTopic:
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
	comments = None
	created = None
	created_by = None
	id = None
	is_closed = None
	is_fixed = None
	title = None
	updated = None
	updated_by = None


class BoardTopicComment:
	"""VK Object BoardTopicComment

	attachments - No description
	date - Date when the comment has been added in Unixtime
	from_id - Author ID
	id - Comment ID
	real_offset - Real position of the comment
	text - Comment text
	can_edit - Information whether current user can edit the comment
	likes - No description
	"""
	attachments = None
	date = None
	from_id = None
	id = None
	real_offset = None
	text = None
	can_edit = None
	likes = None


class BoardTopicPoll:
	"""VK Object BoardTopicPoll

	owner_id - Poll owner's ID
	poll_id - Poll ID
	created - Date when poll has been created in Unixtime
	is_closed - Information whether the poll is closed
	question - Poll question
	votes - Votes number
	answer_id - Current user's answer ID
	answers - No description
	"""
	owner_id = None
	poll_id = None
	created = None
	is_closed = None
	question = None
	votes = None
	answer_id = None
	answers = None


class CallbaCkBoardPostDelete:
	"""VK Object CallbaCkBoardPostDelete

	topic_owner_id - No description
	topic_id - No description
	id - No description
	"""
	topic_owner_id = None
	topic_id = None
	id = None


class CallbaCkConfirmationMessage:
	"""VK Object CallbaCkConfirmationMessage

	type - No description
	group_id - No description
	secret - No description
	"""
	type = None
	group_id = None
	secret = None


class CallbaCkDonutMoneyWithdraw:
	"""VK Object CallbaCkDonutMoneyWithdraw

	amount - No description
	amount_without_fee - No description
	"""
	amount = None
	amount_without_fee = None


class CallbaCkDonutMoneyWithdrawError:
	"""VK Object CallbaCkDonutMoneyWithdrawError

	reason - No description
	"""
	reason = None


class CallbaCkDonutSubsCriptionCanCelled:
	"""VK Object CallbaCkDonutSubsCriptionCanCelled

	user_id - No description
	"""
	user_id = None


class CallbaCkDonutSubsCriptionCreate:
	"""VK Object CallbaCkDonutSubsCriptionCreate

	user_id - No description
	amount - No description
	amount_without_fee - No description
	"""
	user_id = None
	amount = None
	amount_without_fee = None


class CallbaCkDonutSubsCriptionExpired:
	"""VK Object CallbaCkDonutSubsCriptionExpired

	user_id - No description
	"""
	user_id = None


class CallbaCkDonutSubsCriptionPriCeChanged:
	"""VK Object CallbaCkDonutSubsCriptionPriCeChanged

	user_id - No description
	amount_old - No description
	amount_new - No description
	amount_diff - No description
	amount_diff_without_fee - No description
	"""
	user_id = None
	amount_old = None
	amount_new = None
	amount_diff = None
	amount_diff_without_fee = None


class CallbaCkDonutSubsCriptionProlonged:
	"""VK Object CallbaCkDonutSubsCriptionProlonged

	user_id - No description
	amount - No description
	amount_without_fee - No description
	"""
	user_id = None
	amount = None
	amount_without_fee = None


class CallbaCkGroupChangePhoto:
	"""VK Object CallbaCkGroupChangePhoto

	user_id - No description
	photo - No description
	"""
	user_id = None
	photo = None


class CallbaCkGroupChangeSettings:
	"""VK Object CallbaCkGroupChangeSettings

	user_id - No description
	self - No description
	"""
	user_id = None
	self = None


class CallbaCkGroupJoin:
	"""VK Object CallbaCkGroupJoin

	user_id - No description
	join_type - No description
	"""
	user_id = None
	join_type = None


class CallbaCkGroupJoinType:
	"""VK Object CallbaCkGroupJoinType

	join - None
	unsure - None
	accepted - None
	approved - None
	request - None
	"""
	join = 0
	unsure = 1
	accepted = 2
	approved = 3
	request = 4


class CallbaCkGroupLeave:
	"""VK Object CallbaCkGroupLeave

	user_id - No description
	self - No description
	"""
	user_id = None
	self = None
NoneNone

class CallbaCkGroupOffiCersEdit:
	"""VK Object CallbaCkGroupOffiCersEdit

	admin_id - No description
	user_id - No description
	level_old - No description
	level_new - No description
	"""
	admin_id = None
	user_id = None
	level_old = None
	level_new = None


class CallbaCkGroupSettingsChanges:
	"""VK Object CallbaCkGroupSettingsChanges

	title - No description
	description - No description
	access - No description
	screen_name - No description
	public_category - No description
	public_subcategory - No description
	age_limits - No description
	website - No description
	enable_status_default - No description
	enable_audio - No description
	enable_video - No description
	enable_photo - No description
	enable_market - No description
	"""
	title = None
	description = None
	access = None
	screen_name = None
	public_category = None
	public_subcategory = None
	age_limits = None
	website = None
	enable_status_default = None
	enable_audio = None
	enable_video = None
	enable_photo = None
	enable_market = None


class CallbaCkLikeAddRemove:
	"""VK Object CallbaCkLikeAddRemove

	liker_id - No description
	object_type - No description
	object_owner_id - No description
	object_id - No description
	post_id - No description
	thread_reply_id - No description
	"""
	liker_id = None
	object_type = None
	object_owner_id = None
	object_id = None
	post_id = None
	thread_reply_id = None


class CallbaCkMarketComment:
	"""VK Object CallbaCkMarketComment

	id - No description
	from_id - No description
	date - No description
	text - No description
	market_owner_od - No description
	photo_id - No description
	"""
	id = None
	from_id = None
	date = None
	text = None
	market_owner_od = None
	photo_id = None


class CallbaCkMarketCommentDelete:
	"""VK Object CallbaCkMarketCommentDelete

	owner_id - No description
	id - No description
	user_id - No description
	item_id - No description
	"""
	owner_id = None
	id = None
	user_id = None
	item_id = None


class CallbaCkMessageAllow:
	"""VK Object CallbaCkMessageAllow

	user_id - No description
	key - No description
	"""
	user_id = None
	key = None


class CallbaCkMessageBase:
	"""VK Object CallbaCkMessageBase

	type - No description
	object - No description
	group_id - No description
	"""
	type = None
	object = None
	group_id = None


class CallbaCkMessageDeny:
	"""VK Object CallbaCkMessageDeny

	user_id - No description
	"""
	user_id = None


class CallbaCkMessageType:
	"""VK Object CallbaCkMessageType

	audio_new - None
	board_post_new - None
	board_post_edit - None
	board_post_restore - None
	board_post_delete - None
	confirmation - None
	group_leave - None
	group_join - None
	group_change_photo - None
	group_change_settings - None
	group_officers_edit - None
	lead_forms_new - None
	market_comment_new - None
	market_comment_delete - None
	market_comment_edit - None
	market_comment_restore - None
	message_allow - None
	message_new - None
	message_deny - None
	message_read - None
	message_reply - None
	message_edit - None
	message_typing_state - None
	messages_edit - None
	photo_new - None
	photo_comment_new - None
	photo_comment_delete - None
	photo_comment_edit - None
	photo_comment_restore - None
	poll_vote_new - None
	user_block - None
	user_unblock - None
	video_new - None
	video_comment_new - None
	video_comment_delete - None
	video_comment_edit - None
	video_comment_restore - None
	wall_post_new - None
	wall_reply_new - None
	wall_reply_edit - None
	wall_reply_delete - None
	wall_reply_restore - None
	wall_repost - None
	"""
	audio_new = 0
	board_post_new = 1
	board_post_edit = 2
	board_post_restore = 3
	board_post_delete = 4
	confirmation = 5
	group_leave = 6
	group_join = 7
	group_change_photo = 8
	group_change_settings = 9
	group_officers_edit = 10
	lead_forms_new = 11
	market_comment_new = 12
	market_comment_delete = 13
	market_comment_edit = 14
	market_comment_restore = 15
	message_allow = 16
	message_new = 17
	message_deny = 18
	message_read = 19
	message_reply = 20
	message_edit = 21
	message_typing_state = 22
	messages_edit = 23
	photo_new = 24
	photo_comment_new = 25
	photo_comment_delete = 26
	photo_comment_edit = 27
	photo_comment_restore = 28
	poll_vote_new = 29
	user_block = 30
	user_unblock = 31
	video_new = 32
	video_comment_new = 33
	video_comment_delete = 34
	video_comment_edit = 35
	video_comment_restore = 36
	wall_post_new = 37
	wall_reply_new = 38
	wall_reply_edit = 39
	wall_reply_delete = 40
	wall_reply_restore = 41
	wall_repost = 42


class CallbaCkPhotoComment:
	"""VK Object CallbaCkPhotoComment

	id - No description
	from_id - No description
	date - No description
	text - No description
	photo_owner_od - No description
	"""
	id = None
	from_id = None
	date = None
	text = None
	photo_owner_od = None


class CallbaCkPhotoCommentDelete:
	"""VK Object CallbaCkPhotoCommentDelete

	id - No description
	owner_id - No description
	user_id - No description
	photo_id - No description
	"""
	id = None
	owner_id = None
	user_id = None
	photo_id = None


class CallbaCkPollVoteNew:
	"""VK Object CallbaCkPollVoteNew

	owner_id - No description
	poll_id - No description
	option_id - No description
	user_id - No description
	"""
	owner_id = None
	poll_id = None
	option_id = None
	user_id = None


class CallbaCkQrSCan:
	"""VK Object CallbaCkQrSCan

	user_id - No description
	data - No description
	type - No description
	subtype - No description
	reread - No description
	"""
	user_id = None
	data = None
	type = None
	subtype = None
	reread = None


class CallbaCkUserBloCk:
	"""VK Object CallbaCkUserBloCk

	admin_id - No description
	user_id - No description
	unblock_date - No description
	reason - No description
	comment - No description
	"""
	admin_id = None
	user_id = None
	unblock_date = None
	reason = None
	comment = None


class CallbaCkUserUnbloCk:
	"""VK Object CallbaCkUserUnbloCk

	admin_id - No description
	user_id - No description
	by_end_date - No description
	"""
	admin_id = None
	user_id = None
	by_end_date = None


class CallbaCkVideoComment:
	"""VK Object CallbaCkVideoComment

	id - No description
	from_id - No description
	date - No description
	text - No description
	video_owner_od - No description
	"""
	id = None
	from_id = None
	date = None
	text = None
	video_owner_od = None


class CallbaCkVideoCommentDelete:
	"""VK Object CallbaCkVideoCommentDelete

	id - No description
	owner_id - No description
	user_id - No description
	video_id - No description
	"""
	id = None
	owner_id = None
	user_id = None
	video_id = None


class CallbaCkWallCommentDelete:
	"""VK Object CallbaCkWallCommentDelete

	owner_id - No description
	id - No description
	user_id - No description
	post_id - No description
	"""
	owner_id = None
	id = None
	user_id = None
	post_id = None


class CallsCall:
	"""VK Object CallsCall

	duration - Call duration
	initiator_id - Caller initiator
	receiver_id - Caller receiver
	state - No description
	time - Timestamp for call
	video - Was this call initiated as video call
	"""
	duration = None
	initiator_id = None
	receiver_id = None
	state = None
	time = None
	video = None


class CallsEndState:
	"""VK Object CallsEndState

	canceled_by_initiator - None
	canceled_by_receiver - None
	reached - None
	"""
	canceled_by_initiator = 0
	canceled_by_receiver = 1
	reached = 2


class CallsPartiCipants:
	"""VK Object CallsPartiCipants

	list - No description
	count - Participants count
	"""
	list = None
	count = None


class CommentThread:
	"""VK Object CommentThread

	can_post - Information whether current user can comment the post
	count - Comments number
	groups_can_post - Information whether groups can comment the post
	items - No description
	show_reply_button - Information whether recommended to display reply button
	"""
	can_post = None
	count = None
	groups_can_post = None
	items = None
	show_reply_button = None


class DatabaseCity:
	"""VK Object DatabaseCity

	area - Area title
	region - Region title
	important - Information whether the city is included in important cities list
	"""
	area = <built-in function iter>
	region = <built-in function iter>
	important = <built-in function iter>


class DatabaseFaculty:
	"""VK Object DatabaseFaculty

	id - Faculty ID
	title - Faculty title
	"""
	id = None
	title = None


class DatabaseRegion:
	"""VK Object DatabaseRegion

	id - Region ID
	title - Region title
	"""
	id = None
	title = None


class DatabaseSchool:
	"""VK Object DatabaseSchool

	id - School ID
	title - School title
	"""
	id = None
	title = None


class DatabaseStation:
	"""VK Object DatabaseStation

	city_id - City ID
	color - Hex color code without #
	id - Station ID
	name - Station name
	"""
	city_id = None
	color = None
	id = None
	name = None


class DatabaseUniversity:
	"""VK Object DatabaseUniversity

	id - University ID
	title - University title
	"""
	id = None
	title = None


class DocsDoc:
	"""VK Object DocsDoc

	id - Document ID
	owner_id - Document owner ID
	title - Document title
	size - File size in bites
	ext - File extension
	url - File URL
	date - Date when file has been uploaded in Unixtime
	type - Document type
	preview - No description
	is_licensed - No description
	access_key - Access key for the document
	tags - Document tags
	"""
	id = None
	owner_id = None
	title = None
	size = None
	ext = None
	url = None
	date = None
	type = None
	preview = None
	is_licensed = None
	access_key = None
	tags = None


class DocsDocAttachmentType:
	"""VK Object DocsDocAttachmentType

	doc - None
	graffiti - None
	audio_message - None
	"""
	doc = 0
	graffiti = 1
	audio_message = 2


class DocsDocPreview:
	"""VK Object DocsDocPreview

	audio_msg - No description
	graffiti - No description
	photo - No description
	video - No description
	"""
	audio_msg = None
	graffiti = None
	photo = None
	video = None


class DocsDocPreviewAuDioMsg:
	"""VK Object DocsDocPreviewAuDioMsg

	duration - Audio message duration in seconds
	link_mp3 - MP3 file URL
	link_ogg - OGG file URL
	waveform - No description
	"""
	duration = None
	link_mp3 = None
	link_ogg = None
	waveform = None


class DocsDocPreviewGraffiti:
	"""VK Object DocsDocPreviewGraffiti

	src - Graffiti file URL
	width - Graffiti width
	height - Graffiti height
	"""
	src = None
	width = None
	height = None


class DocsDocPreviewPhoto:
	"""VK Object DocsDocPreviewPhoto

	sizes - No description
	"""
	sizes = None


class DocsDocPreviewPhotoSizes:
	"""VK Object DocsDocPreviewPhotoSizes

	src - URL of the image
	width - Width in px
	height - Height in px
	type - No description
	"""
	src = None
	width = None
	height = None
	type = None


class DocsDocPreviewViDeo:
	"""VK Object DocsDocPreviewViDeo

	src - Video URL
	width - Video's width in pixels
	height - Video's height in pixels
	file_size - Video file size in bites
	"""
	src = None
	width = None
	height = None
	file_size = None


class DocsDocTypes:
	"""VK Object DocsDocTypes

	id - Doc type ID
	name - Doc type title
	count - Number of docs
	"""
	id = None
	name = None
	count = None


class DonutDonatorSubscriptionInfo:
	"""VK Object DonutDonatorSubscriptionInfo

	owner_id - No description
	next_payment_date - No description
	amount - No description
	status - No description
	"""
	owner_id = None
	next_payment_date = None
	amount = None
	status = None


class EvEntsEvEntAttach:
	"""VK Object EvEntsEvEntAttach

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	id - event ID
	is_favorite - is favorite
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address = None
	button_text = None
	friends = None
	id = None
	is_favorite = None
	member_status = None
	text = None
	time = None


class FaveBookmark:
	"""VK Object FaveBookmark

	added_date - Timestamp, when this item was bookmarked
	link - No description
	post - No description
	product - No description
	seen - Has user seen this item
	tags - No description
	type - Item type
	video - No description
	"""
	added_date = None
	link = None
	post = None
	product = None
	seen = None
	tags = None
	type = None
	video = None


class FaveBookmarkType:
	"""VK Object FaveBookmarkType

	post - None
	video - None
	product - None
	article - None
	link - None
	"""
	post = 0
	video = 1
	product = 2
	article = 3
	link = 4


class FavePage:
	"""VK Object FavePage

	description - Some info about user or group
	group - No description
	tags - No description
	type - Item type
	updated_date - Timestamp, when this page was bookmarked
	user - No description
	"""
	description = None
	group = None
	tags = None
	type = None
	updated_date = None
	user = None


class FavePageType:
	"""VK Object FavePageType

	user - None
	group - None
	hints - None
	"""
	user = 0
	group = 1
	hints = 2


class FaveTag:
	"""VK Object FaveTag

	id - Tag id
	name - Tag name
	"""
	id = None
	name = None


class FriendsFriendExtendedStatus:
	"""VK Object FriendsFriendExtendedStatus

	is_request_unread - Is friend request from other user unread
	"""
	is_request_unread = <built-in function iter>


class FriendsFriendStatus:
	"""VK Object FriendsFriendStatus

	friend_status - No description
	sign - MD5 hash for the result validation
	user_id - User ID
	"""
	friend_status = None
	sign = None
	user_id = None
None

class FriendsFriendsList:
	"""VK Object FriendsFriendsList

	id - List ID
	name - List title
	"""
	id = None
	name = None


class FriendsMutualFriend:
	"""VK Object FriendsMutualFriend

	common_count - Total mutual friends number
	common_friends - No description
	id - User ID
	"""
	common_count = None
	common_friends = None
	id = None


class FriendsRequests:
	"""VK Object FriendsRequests

	from - ID of the user by whom friend has been suggested
	mutual - No description
	user_id - User ID
	"""
	_from = None
	mutual = None
	user_id = None


class FriendsRequestsMutual:
	"""VK Object FriendsRequestsMutual

	count - Total mutual friends number
	users - No description
	"""
	count = None
	users = None


class FriendsRequestsXtrMessage:
	"""VK Object FriendsRequestsXtrMessage

	from - ID of the user by whom friend has been suggested
	message - Message sent with a request
	mutual - No description
	user_id - User ID
	"""
	_from = None
	message = None
	mutual = None
	user_id = None


class FriendsUserXtrLists:
	"""VK Object FriendsUserXtrLists

	lists - No description
	"""
	lists = <built-in function iter>


class FriendsUserXtrPhone:
	"""VK Object FriendsUserXtrPhone

	phone - User phone
	"""
	phone = <built-in function iter>


class GiftsGift:
	"""VK Object GiftsGift

	date - Date when gist has been sent in Unixtime
	from_id - Gift sender ID
	gift - No description
	gift_hash - Hash
	id - Gift ID
	message - Comment text
	privacy - No description
	"""
	date = None
	from_id = None
	gift = None
	gift_hash = None
	id = None
	message = None
	privacy = None
None

class GiftsLayout:
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
	id = None
	thumb_512 = None
	thumb_256 = None
	thumb_48 = None
	thumb_96 = None
	stickers_product_id = None
	is_stickers_style = None
	build_id = None
	keywords = None


class GroupsAddress:
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
	additional_address = None
	address = None
	city_id = None
	country_id = None
	distance = None
	id = None
	latitude = None
	longitude = None
	metro_station_id = None
	phone = None
	time_offset = None
	timetable = None
	title = None
	work_info_status = None


class GroupsAddressTimetable:
	"""VK Object GroupsAddressTimetable

	fri - Timetable for friday
	mon - Timetable for monday
	sat - Timetable for saturday
	sun - Timetable for sunday
	thu - Timetable for thursday
	tue - Timetable for tuesday
	wed - Timetable for wednesday
	"""
	fri = None
	mon = None
	sat = None
	sun = None
	thu = None
	tue = None
	wed = None


class GroupsAddressTimetableDay:
	"""VK Object GroupsAddressTimetableDay

	break_close_time - Close time of the break in minutes
	break_open_time - Start time of the break in minutes
	close_time - Close time in minutes
	open_time - Open time in minutes
	"""
	break_close_time = None
	break_open_time = None
	close_time = None
	open_time = None


class GroupsAddressWorkInfoStatus:
	"""VK Object GroupsAddressWorkInfoStatus

	no_information - None
	temporarily_closed - None
	always_opened - None
	timetable - None
	forever_closed - None
	"""
	no_information = 0
	temporarily_closed = 1
	always_opened = 2
	timetable = 3
	forever_closed = 4


class GroupsAddressesInfo:
	"""VK Object GroupsAddressesInfo

	is_enabled - Information whether addresses is enabled
	main_address_id - Main address id for group
	"""
	is_enabled = None
	main_address_id = None


class GroupsBanInfo:
	"""VK Object GroupsBanInfo

	admin_id - Administrator ID
	comment - Comment for a ban
	comment_visible - Show comment for user
	is_closed - No description
	date - Date when user has been added to blacklist in Unixtime
	end_date - Date when user will be removed from blacklist in Unixtime
	reason - No description
	"""
	admin_id = None
	comment = None
	comment_visible = None
	is_closed = None
	date = None
	end_date = None
	reason = None
None

class GroupsBannedItem:
	"""VK Object GroupsBannedItem

	"""


class GroupsCallbackServer:
	"""VK Object GroupsCallbackServer

	id - No description
	title - No description
	creator_id - No description
	url - No description
	secret_key - No description
	status - No description
	"""
	id = None
	title = None
	creator_id = None
	url = None
	secret_key = None
	status = None


class GroupsCallbackSettinGs:
	"""VK Object GroupsCallbackSettinGs

	api_version - API version used for the events
	events - No description
	"""
	api_version = None
	events = None


class GroupsContactsItem:
	"""VK Object GroupsContactsItem

	user_id - User ID
	desc - Contact description
	phone - Contact phone
	email - Contact email
	"""
	user_id = None
	desc = None
	phone = None
	email = None


class GroupsCountersGroup:
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
	addresses = None
	albums = None
	audios = None
	audio_playlists = None
	docs = None
	market = None
	photos = None
	topics = None
	videos = None


class GroupsCover:
	"""VK Object GroupsCover

	enabled - Information whether cover is enabled
	images - No description
	"""
	enabled = None
	images = None


class GroupsFields:
	"""VK Object GroupsFields

	market - None
	member_status - None
	is_favorite - None
	is_subscribed - None
	is_subscribed_podcasts - None
	can_subscribe_podcasts - None
	city - None
	country - None
	verified - None
	description - None
	wiki_page - None
	members_count - None
	requests_count - None
	counters - None
	cover - None
	can_post - None
	can_suggest - None
	can_upload_story - None
	can_upload_doc - None
	can_upload_video - None
	can_see_all_posts - None
	can_create_topic - None
	activity - None
	fixed_post - None
	has_photo - None
	status - None
	main_album_id - None
	links - None
	contacts - None
	site - None
	main_section - None
	secondary_section - None
	wall - None
	trending - None
	can_message - None
	is_market_cart_enabled - None
	is_messages_blocked - None
	can_send_notify - None
	has_group_channel - None
	group_channel - None
	online_status - None
	start_date - None
	finish_date - None
	age_limits - None
	ban_info - None
	action_button - None
	author_id - None
	phone - None
	has_market_app - None
	addresses - None
	live_covers - None
	is_adult - None
	can_subscribe_posts - None
	warning_notification - None
	msg_push_allowed - None
	stories_archive_count - None
	video_live_level - None
	video_live_count - None
	clips_count - None
	is_business - None
	"""
	market = 0
	member_status = 1
	is_favorite = 2
	is_subscribed = 3
	is_subscribed_podcasts = 4
	can_subscribe_podcasts = 5
	city = 6
	country = 7
	verified = 8
	description = 9
	wiki_page = 10
	members_count = 11
	requests_count = 12
	counters = 13
	cover = 14
	can_post = 15
	can_suggest = 16
	can_upload_story = 17
	can_upload_doc = 18
	can_upload_video = 19
	can_see_all_posts = 20
	can_create_topic = 21
	activity = 22
	fixed_post = 23
	has_photo = 24
	status = 25
	main_album_id = 26
	links = 27
	contacts = 28
	site = 29
	main_section = 30
	secondary_section = 31
	wall = 32
	trending = 33
	can_message = 34
	is_market_cart_enabled = 35
	is_messages_blocked = 36
	can_send_notify = 37
	has_group_channel = 38
	group_channel = 39
	online_status = 40
	start_date = 41
	finish_date = 42
	age_limits = 43
	ban_info = 44
	action_button = 45
	author_id = 46
	phone = 47
	has_market_app = 48
	addresses = 49
	live_covers = 50
	is_adult = 51
	can_subscribe_posts = 52
	warning_notification = 53
	msg_push_allowed = 54
	stories_archive_count = 55
	video_live_level = 56
	video_live_count = 57
	clips_count = 58
	is_business = 59


class GroupsFilter:
	"""VK Object GroupsFilter

	admin - None
	editor - None
	moder - None
	advertiser - None
	groups - None
	publics - None
	events - None
	has_addresses - None
	"""
	admin = 0
	editor = 1
	moder = 2
	advertiser = 3
	groups = 4
	publics = 5
	events = 6
	has_addresses = 7


class GroupsGroup:
	"""VK Object GroupsGroup

	id - Community ID
	name - Community name
	screen_name - Domain of the community page
	is_closed - No description
	type - No description
	is_admin - Information whether current user is administrator
	admin_level - No description
	is_member - Information whether current user is member
	is_advertiser - Information whether current user is advertiser
	start_date - Start date in Unixtime format
	finish_date - Finish date in Unixtime format
	deactivated - Information whether community is banned
	photo_50 - URL of square photo of the community with 50 pixels in width
	photo_100 - URL of square photo of the community with 100 pixels in width
	photo_200 - URL of square photo of the community with 200 pixels in width
	"""
	id = None
	name = None
	screen_name = None
	is_closed = None
	type = None
	is_admin = None
	admin_level = None
	is_member = None
	is_advertiser = None
	start_date = None
	finish_date = None
	deactivated = None
	photo_50 = None
	photo_100 = None
	photo_200 = None
NoneNoneNone

class GroupsGroupAttach:
	"""VK Object GroupsGroupAttach

	id - group ID
	text - text of attach
	status - activity or category of group
	size - size of group
	is_favorite - is favorite
	"""
	id = None
	text = None
	status = None
	size = None
	is_favorite = None
None

class GroupsGroupBanInfo:
	"""VK Object GroupsGroupBanInfo

	comment - Ban comment
	end_date - End date of ban in Unixtime
	reason - No description
	"""
	comment = None
	end_date = None
	reason = None


class GroupsGroupCateGory:
	"""VK Object GroupsGroupCateGory

	id - Category ID
	name - Category name
	subcategories - No description
	"""
	id = None
	name = None
	subcategories = None


class GroupsGroupCateGoryFull:
	"""VK Object GroupsGroupCateGoryFull

	id - Category ID
	name - Category name
	page_count - Pages number
	page_previews - No description
	subcategories - No description
	"""
	id = None
	name = None
	page_count = None
	page_previews = None
	subcategories = None


class GroupsGroupCateGoryType:
	"""VK Object GroupsGroupCateGoryType

	id - No description
	name - No description
	"""
	id = None
	name = None
None

class GroupsGroupFull:
	"""VK Object GroupsGroupFull

	market - No description
	member_status - Current user's member status
	is_adult - Information whether community is adult
	is_hidden_from_feed - Information whether community is hidden from current user's newsfeed
	is_favorite - Information whether community is in faves
	is_subscribed - Information whether current user is subscribed
	city - No description
	country - No description
	verified - Information whether community is verified
	description - Community description
	wiki_page - Community's main wiki page title
	members_count - Community members number
	requests_count - The number of incoming requests to the community
	video_live_level - Community level live streams achievements
	video_live_count - Number of community's live streams
	clips_count - Number of community's clips
	counters - No description
	cover - No description
	can_post - Information whether current user can post on community's wall
	can_suggest - No description
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
	status_audio - No description
	main_album_id - Community's main photo album ID
	links - No description
	contacts - No description
	wall - Information about wall status in community
	site - Community's website
	main_section - No description
	secondary_section - No description
	trending - Information whether the community has a "fire" pictogram.
	can_message - Information whether current user can send a message to community
	is_messages_blocked - Information whether community can send a message to current user
	can_send_notify - Information whether community can send notifications by phone number to current user
	online_status - Status of replies in community messages
	invited_by - Inviter ID
	age_limits - Information whether age limit
	ban_info - User ban info
	has_market_app - Information whether community has installed market app
	using_vkpay_market_app - No description
	has_group_channel - No description
	addresses - Info about addresses in groups
	is_subscribed_podcasts - Information whether current user is subscribed to podcasts
	can_subscribe_podcasts - Owner in whitelist or not
	can_subscribe_posts - Can subscribe to wall
	live_covers - Live covers state
	stories_archive_count - No description
	"""
	market = <built-in function iter>
	member_status = <built-in function iter>
	is_adult = <built-in function iter>
	is_hidden_from_feed = <built-in function iter>
	is_favorite = <built-in function iter>
	is_subscribed = <built-in function iter>
	city = <built-in function iter>
	country = <built-in function iter>
	verified = <built-in function iter>
	description = <built-in function iter>
	wiki_page = <built-in function iter>
	members_count = <built-in function iter>
	requests_count = <built-in function iter>
	video_live_level = <built-in function iter>
	video_live_count = <built-in function iter>
	clips_count = <built-in function iter>
	counters = <built-in function iter>
	cover = <built-in function iter>
	can_post = <built-in function iter>
	can_suggest = <built-in function iter>
	can_upload_story = <built-in function iter>
	can_upload_doc = <built-in function iter>
	can_upload_video = <built-in function iter>
	can_see_all_posts = <built-in function iter>
	can_create_topic = <built-in function iter>
	activity = <built-in function iter>
	fixed_post = <built-in function iter>
	has_photo = <built-in function iter>
	crop_photo = <built-in function iter>
	status = <built-in function iter>
	status_audio = <built-in function iter>
	main_album_id = <built-in function iter>
	links = <built-in function iter>
	contacts = <built-in function iter>
	wall = <built-in function iter>
	site = <built-in function iter>
	main_section = <built-in function iter>
	secondary_section = <built-in function iter>
	trending = <built-in function iter>
	can_message = <built-in function iter>
	is_messages_blocked = <built-in function iter>
	can_send_notify = <built-in function iter>
	online_status = <built-in function iter>
	invited_by = <built-in function iter>
	age_limits = <built-in function iter>
	ban_info = <built-in function iter>
	has_market_app = <built-in function iter>
	using_vkpay_market_app = <built-in function iter>
	has_group_channel = <built-in function iter>
	addresses = <built-in function iter>
	is_subscribed_podcasts = <built-in function iter>
	can_subscribe_podcasts = <built-in function iter>
	can_subscribe_posts = <built-in function iter>
	live_covers = <built-in function iter>
	stories_archive_count = <built-in function iter>
NoneNoneNoneNone

class GroupsGroupLink:
	"""VK Object GroupsGroupLink

	name - Link label
	desc - Link description
	edit_title - Information whether the title can be edited
	id - Link ID
	image_processing - Information whether the image on processing
	url - Link URL
	"""
	name = None
	desc = None
	edit_title = None
	id = None
	image_processing = None
	url = None
NoneNone

class GroupsGroupPublicCateGoryList:
	"""VK Object GroupsGroupPublicCateGoryList

	id - No description
	name - No description
	subcategories - No description
	"""
	id = None
	name = None
	subcategories = None


class GroupsGroupRole:
	"""VK Object GroupsGroupRole

	moderator - None
	editor - None
	administrator - None
	advertiser - None
	"""
	moderator = 0
	editor = 1
	administrator = 2
	advertiser = 3


class GroupsGroupSubject:
	"""VK Object GroupsGroupSubject

	auto - None
	activity holidays - None
	business - None
	pets - None
	health - None
	dating and communication - None
	games - None
	it - None
	cinema - None
	beauty and fashion - None
	cooking - None
	art and culture - None
	literature - None
	mobile services and internet - None
	music - None
	science and technology - None
	real estate - None
	news and media - None
	security - None
	education - None
	home and renovations - None
	politics - None
	food - None
	industry - None
	travel - None
	work - None
	entertainment - None
	religion - None
	family - None
	sports - None
	insurance - None
	television - None
	goods and services - None
	hobbies - None
	finance - None
	photo - None
	esoterics - None
	electronics and appliances - None
	erotic - None
	humor - None
	society_humanities - None
	design and graphics - None
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
None

class GroupsGroupTaG:
	"""VK Object GroupsGroupTaG

	id - No description
	name - No description
	color - No description
	uses - No description
	"""
	id = None
	name = None
	color = None
	uses = None
None

class GroupsGroupType:
	"""VK Object GroupsGroupType

	group - None
	page - None
	event - None
	"""
	group = 0
	page = 1
	event = 2
NoneNoneNone

class GroupsGroupsArray:
	"""VK Object GroupsGroupsArray

	count - Communities number
	items - No description
	"""
	count = None
	items = None


class GroupsLinksItem:
	"""VK Object GroupsLinksItem

	desc - Link description
	edit_title - Information whether the link title can be edited
	id - Link ID
	name - Link title
	photo_100 - URL of square image of the link with 100 pixels in width
	photo_50 - URL of square image of the link with 50 pixels in width
	url - Link URL
	"""
	desc = None
	edit_title = None
	id = None
	name = None
	photo_100 = None
	photo_50 = None
	url = None


class GroupsLiveCovers:
	"""VK Object GroupsLiveCovers

	is_enabled - Information whether live covers is enabled
	is_scalable - Information whether live covers photo scaling is enabled
	story_ids - No description
	"""
	is_enabled = None
	is_scalable = None
	story_ids = None


class GroupsLonGPollEvents:
	"""VK Object GroupsLonGPollEvents

	audio_new - No description
	board_post_delete - No description
	board_post_edit - No description
	board_post_new - No description
	board_post_restore - No description
	group_change_photo - No description
	group_change_settings - No description
	group_join - No description
	group_leave - No description
	group_officers_edit - No description
	lead_forms_new - No description
	market_comment_delete - No description
	market_comment_edit - No description
	market_comment_new - No description
	market_comment_restore - No description
	market_order_new - No description
	market_order_edit - No description
	message_allow - No description
	message_deny - No description
	message_new - No description
	message_read - No description
	message_reply - No description
	message_typing_state - No description
	message_edit - No description
	photo_comment_delete - No description
	photo_comment_edit - No description
	photo_comment_new - No description
	photo_comment_restore - No description
	photo_new - No description
	poll_vote_new - No description
	user_block - No description
	user_unblock - No description
	video_comment_delete - No description
	video_comment_edit - No description
	video_comment_new - No description
	video_comment_restore - No description
	video_new - No description
	wall_post_new - No description
	wall_reply_delete - No description
	wall_reply_edit - No description
	wall_reply_new - No description
	wall_reply_restore - No description
	wall_repost - No description
	donut_subscription_create - No description
	donut_subscription_prolonged - No description
	donut_subscription_cancelled - No description
	donut_subscription_expired - No description
	donut_subscription_price_changed - No description
	donut_money_withdraw - No description
	donut_money_withdraw_error - No description
	"""
	audio_new = None
	board_post_delete = None
	board_post_edit = None
	board_post_new = None
	board_post_restore = None
	group_change_photo = None
	group_change_settings = None
	group_join = None
	group_leave = None
	group_officers_edit = None
	lead_forms_new = None
	market_comment_delete = None
	market_comment_edit = None
	market_comment_new = None
	market_comment_restore = None
	market_order_new = None
	market_order_edit = None
	message_allow = None
	message_deny = None
	message_new = None
	message_read = None
	message_reply = None
	message_typing_state = None
	message_edit = None
	photo_comment_delete = None
	photo_comment_edit = None
	photo_comment_new = None
	photo_comment_restore = None
	photo_new = None
	poll_vote_new = None
	user_block = None
	user_unblock = None
	video_comment_delete = None
	video_comment_edit = None
	video_comment_new = None
	video_comment_restore = None
	video_new = None
	wall_post_new = None
	wall_reply_delete = None
	wall_reply_edit = None
	wall_reply_new = None
	wall_reply_restore = None
	wall_repost = None
	donut_subscription_create = None
	donut_subscription_prolonged = None
	donut_subscription_cancelled = None
	donut_subscription_expired = None
	donut_subscription_price_changed = None
	donut_money_withdraw = None
	donut_money_withdraw_error = None


class GroupsLonGPollServer:
	"""VK Object GroupsLonGPollServer

	key - Long Poll key
	server - Long Poll server address
	ts - Number of the last event
	"""
	key = None
	server = None
	ts = None


class GroupsLonGPollSettinGs:
	"""VK Object GroupsLonGPollSettinGs

	api_version - API version used for the events
	events - No description
	is_enabled - Shows whether Long Poll is enabled
	"""
	api_version = None
	events = None
	is_enabled = None


class GroupsMarketInfo:
	"""VK Object GroupsMarketInfo

	contact_id - Contact person ID
	currency - No description
	currency_text - Currency name
	enabled - Information whether the market is enabled
	main_album_id - Main market album ID
	price_max - Maximum price
	price_min - Minimum price
	"""
	contact_id = None
	currency = None
	currency_text = None
	enabled = None
	main_album_id = None
	price_max = None
	price_min = None


class GroupsMarketState:
	"""VK Object GroupsMarketState

	none - None
	basic - None
	advanced - None
	"""
	none = 0
	basic = 1
	advanced = 2


class GroupsMemberRole:
	"""VK Object GroupsMemberRole

	id - User ID
	permissions - No description
	role - No description
	"""
	id = None
	permissions = None
	role = None


class GroupsMemberRolePermission:
	"""VK Object GroupsMemberRolePermission

	ads - None
	"""
	ads = 0


class GroupsMemberRoleStatus:
	"""VK Object GroupsMemberRoleStatus

	moderator - None
	editor - None
	administrator - None
	creator - None
	"""
	moderator = 0
	editor = 1
	administrator = 2
	creator = 3


class GroupsMemberStatus:
	"""VK Object GroupsMemberStatus

	member - Information whether user is a member of the group
	user_id - User ID
	"""
	member = None
	user_id = None


class GroupsMemberStatusFull:
	"""VK Object GroupsMemberStatusFull

	can_invite - Information whether user can be invited
	can_recall - Information whether user's invite to the group can be recalled
	invitation - Information whether user has been invited to the group
	member - Information whether user is a member of the group
	request - Information whether user has send request to the group
	user_id - User ID
	"""
	can_invite = None
	can_recall = None
	invitation = None
	member = None
	request = None
	user_id = None


class GroupsOnlineStatus:
	"""VK Object GroupsOnlineStatus

	minutes - Estimated time of answer (for status = answer_mark)
	status - No description
	"""
	minutes = None
	status = None


class GroupsOnlineStatusType:
	"""VK Object GroupsOnlineStatusType

	none - None
	online - None
	answer_mark - None
	"""
	none = 0
	online = 1
	answer_mark = 2


class GroupsOwnerXtrBanInfo:
	"""VK Object GroupsOwnerXtrBanInfo

	ban_info - No description
	group - Information about group if type = group
	profile - Information about group if type = profile
	type - No description
	"""
	ban_info = None
	group = None
	profile = None
	type = None


class GroupsOwnerXtrBanInfoType:
	"""VK Object GroupsOwnerXtrBanInfoType

	group - None
	profile - None
	"""
	group = 0
	profile = 1


class GroupsProfileItem:
	"""VK Object GroupsProfileItem

	id - User id
	photo_50 - Url for user photo
	photo_100 - Url for user photo
	first_name - User first name
	"""
	id = None
	photo_50 = None
	photo_100 = None
	first_name = None


class GroupsRoleOptions:
	"""VK Object GroupsRoleOptions

	moderator - None
	editor - None
	administrator - None
	creator - None
	"""
	moderator = 0
	editor = 1
	administrator = 2
	creator = 3


class GroupsSettinGsTwitter:
	"""VK Object GroupsSettinGsTwitter

	status - No description
	name - No description
	"""
	status = None
	name = None


class GroupsSubjectItem:
	"""VK Object GroupsSubjectItem

	id - Subject ID
	name - Subject title
	"""
	id = None
	name = None


class GroupsTokenPermissionSettinG:
	"""VK Object GroupsTokenPermissionSettinG

	name - No description
	setting - No description
	"""
	name = None
	setting = None


class GroupsUserXtrRole:
	"""VK Object GroupsUserXtrRole

	role - No description
	"""
	role = <built-in function iter>


class LikesType:
	"""VK Object LikesType

	post - None
	comment - None
	photo - None
	audio - None
	video - None
	note - None
	market - None
	photo_comment - None
	video_comment - None
	topic_comment - None
	market_comment - None
	sitepage - None
	"""
	post = 0
	comment = 1
	photo = 2
	audio = 3
	video = 4
	note = 5
	market = 6
	photo_comment = 7
	video_comment = 8
	topic_comment = 9
	market_comment = 10
	sitepage = 11


class LinkTargetObject:
	"""VK Object LinkTargetObject

	type - Object type
	owner_id - Owner ID
	item_id - Item ID
	"""
	type = None
	owner_id = None
	item_id = None


class MarketCurrency:
	"""VK Object MarketCurrency

	id - Currency ID
	name - Currency sign
	"""
	id = None
	name = None


class MarketMarketAlbuM:
	"""VK Object MarketMarketAlbuM

	count - Items number
	id - Market album ID
	owner_id - Market album owner's ID
	photo - No description
	title - Market album title
	updated_time - Date when album has been updated last time in Unixtime
	"""
	count = None
	id = None
	owner_id = None
	photo = None
	title = None
	updated_time = None


class MarketMarketCategory:
	"""VK Object MarketMarketCategory

	"""


class MarketMarketCategoryNested:
	"""VK Object MarketMarketCategoryNested

	id - Category ID
	name - Category name
	parent - No description
	"""
	id = None
	name = None
	parent = None


class MarketMarketCategoryOld:
	"""VK Object MarketMarketCategoryOld

	id - Category ID
	name - Category name
	section - No description
	"""
	id = None
	name = None
	section = None


class MarketMarketCategoryTree:
	"""VK Object MarketMarketCategoryTree

	id - Category ID
	name - Category name
	children - No description
	"""
	id = None
	name = None
	children = None


class MarketMarketIteM:
	"""VK Object MarketMarketIteM

	access_key - Access key for the market item
	availability - No description
	button_title - Title for button for url
	category - No description
	date - Date when the item has been created in Unixtime
	description - Item description
	external_id - No description
	id - Item ID
	is_favorite - No description
	owner_id - Item owner's ID
	price - No description
	thumb_photo - URL of the preview image
	title - Item title
	url - URL to item
	variants_grouping_id - No description
	is_main_variant - No description
	"""
	access_key = None
	availability = None
	button_title = None
	category = None
	date = None
	description = None
	external_id = None
	id = None
	is_favorite = None
	owner_id = None
	price = None
	thumb_photo = None
	title = None
	url = None
	variants_grouping_id = None
	is_main_variant = None
None

class MarketMarketIteMFull:
	"""VK Object MarketMarketIteMFull

	albums_ids - No description
	photos - No description
	can_comment - Information whether current use can comment the item
	can_repost - Information whether current use can repost the item
	likes - No description
	reposts - No description
	views_count - Views number
	wishlist_item_id - Object identifier in wishlist of viewer
	cancel_info - Information for cancel and revert order
	user_agreement_info - User agreement info
	"""
	albums_ids = <built-in function iter>
	photos = <built-in function iter>
	can_comment = <built-in function iter>
	can_repost = <built-in function iter>
	likes = <built-in function iter>
	reposts = <built-in function iter>
	views_count = <built-in function iter>
	wishlist_item_id = <built-in function iter>
	cancel_info = <built-in function iter>
	user_agreement_info = <built-in function iter>


class MarketOrder:
	"""VK Object MarketOrder

	id - No description
	group_id - No description
	user_id - No description
	display_order_id - No description
	date - No description
	status - No description
	items_count - No description
	track_number - No description
	track_link - No description
	comment - No description
	address - No description
	merchant_comment - No description
	weight - No description
	total_price - No description
	preview_order_items - Several order items for preview
	cancel_info - Information for cancel and revert order
	"""
	id = None
	group_id = None
	user_id = None
	display_order_id = None
	date = None
	status = None
	items_count = None
	track_number = None
	track_link = None
	comment = None
	address = None
	merchant_comment = None
	weight = None
	total_price = None
	preview_order_items = None
	cancel_info = None


class MarketOrderIteM:
	"""VK Object MarketOrderIteM

	owner_id - No description
	item_id - No description
	price - No description
	quantity - No description
	item - No description
	title - No description
	photo - No description
	variants - No description
	"""
	owner_id = None
	item_id = None
	price = None
	quantity = None
	item = None
	title = None
	photo = None
	variants = None


class MarketPrice:
	"""VK Object MarketPrice

	amount - Amount
	currency - No description
	discount_rate - No description
	old_amount - No description
	text - Text
	old_amount_text - Textual representation of old price
	"""
	amount = None
	currency = None
	discount_rate = None
	old_amount = None
	text = None
	old_amount_text = None


class MarketSection:
	"""VK Object MarketSection

	id - Section ID
	name - Section name
	"""
	id = None
	name = None


class MediaRestriction:
	"""VK Object MediaRestriction

	text - No description
	title - No description
	button - No description
	always_shown - Need show restriction always or not
	blur - Need blur current video or not
	can_play - Can play video or not
	can_preview - Can preview video or not
	card_icon - No description
	list_icon - No description
	"""
	text = None
	title = None
	button = None
	always_shown = None
	blur = None
	can_play = None
	can_preview = None
	card_icon = None
	list_icon = None


class MessagesAudioMessage:
	"""VK Object MessagesAudioMessage

	access_key - Access key for audio message
	transcript_error - No description
	duration - Audio message duration in seconds
	id - Audio message ID
	link_mp3 - MP3 file URL
	link_ogg - OGG file URL
	owner_id - Audio message owner ID
	waveform - No description
	"""
	access_key = None
	transcript_error = None
	duration = None
	id = None
	link_mp3 = None
	link_ogg = None
	owner_id = None
	waveform = None


class MessagesChat:
	"""VK Object MessagesChat

	admin_id - Chat creator ID
	id - Chat ID
	kicked - Shows that user has been kicked from the chat
	left - Shows that user has been left the chat
	photo_100 - URL of the preview image with 100 px in width
	photo_200 - URL of the preview image with 200 px in width
	photo_50 - URL of the preview image with 50 px in width
	push_settings - No description
	title - Chat title
	type - Chat type
	users - No description
	is_default_photo - If provided photo is default
	"""
	admin_id = None
	id = None
	kicked = None
	left = None
	photo_100 = None
	photo_200 = None
	photo_50 = None
	push_settings = None
	title = None
	type = None
	users = None
	is_default_photo = None


class MessagesChatFull:
	"""VK Object MessagesChatFull

	admin_id - Chat creator ID
	id - Chat ID
	kicked - Shows that user has been kicked from the chat
	left - Shows that user has been left the chat
	photo_100 - URL of the preview image with 100 px in width
	photo_200 - URL of the preview image with 200 px in width
	photo_50 - URL of the preview image with 50 px in width
	push_settings - No description
	title - Chat title
	type - Chat type
	users - No description
	"""
	admin_id = None
	id = None
	kicked = None
	left = None
	photo_100 = None
	photo_200 = None
	photo_50 = None
	push_settings = None
	title = None
	type = None
	users = None


class MessagesChatPreview:
	"""VK Object MessagesChatPreview

	admin_id - No description
	joined - No description
	local_id - No description
	members - No description
	members_count - No description
	title - No description
	is_member - No description
	"""
	admin_id = None
	joined = None
	local_id = None
	members = None
	members_count = None
	title = None
	is_member = None


class MessagesChatPushSettings:
	"""VK Object MessagesChatPushSettings

	disabled_until - Time until that notifications are disabled
	sound - Information whether the sound is on
	"""
	disabled_until = None
	sound = None


class MessagesChatRestrictions:
	"""VK Object MessagesChatRestrictions

	admins_promote_users - Only admins can promote users to admins
	only_admins_edit_info - Only admins can change chat info
	only_admins_edit_pin - Only admins can edit pinned message
	only_admins_invite - Only admins can invite users to this chat
	only_admins_kick - Only admins can kick users from this chat
	"""
	admins_promote_users = None
	only_admins_edit_info = None
	only_admins_edit_pin = None
	only_admins_invite = None
	only_admins_kick = None


class MessagesChatSettings:
	"""VK Object MessagesChatSettings

	members_count - No description
	friends_count - No description
	owner_id - No description
	title - Chat title
	pinned_message - No description
	state - No description
	photo - No description
	admin_ids - Ids of chat admins
	active_ids - No description
	is_group_channel - No description
	acl - No description
	permissions - No description
	is_disappearing - No description
	theme - No description
	disappearing_chat_link - No description
	is_service - No description
	"""
	members_count = None
	friends_count = None
	owner_id = None
	title = None
	pinned_message = None
	state = None
	photo = None
	admin_ids = None
	active_ids = None
	is_group_channel = None
	acl = None
	permissions = None
	is_disappearing = None
	theme = None
	disappearing_chat_link = None
	is_service = None


class MessagesChatSettingsAcl:
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
	can_change_info = None
	can_change_invite_link = None
	can_change_pin = None
	can_invite = None
	can_promote_users = None
	can_see_invite_link = None
	can_moderate = None
	can_copy_chat = None
	can_call = None
	can_use_mass_mentions = None
	can_change_service_type = None


class MessagesChatSettingsPerMissions:
	"""VK Object MessagesChatSettingsPerMissions

	invite - Who can invite users to chat
	change_info - Who can change chat info
	change_pin - Who can change pinned message
	use_mass_mentions - Who can use mass mentions
	see_invite_link - Who can see invite link
	call - Who can make calls
	change_admins - Who can change admins
	"""
	invite = None
	change_info = None
	change_pin = None
	use_mass_mentions = None
	see_invite_link = None
	call = None
	change_admins = None


class MessagesChatSettingsPhoto:
	"""VK Object MessagesChatSettingsPhoto

	photo_50 - URL of the preview image with 50px in width
	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	is_default_photo - If provided photo is default
	"""
	photo_50 = None
	photo_100 = None
	photo_200 = None
	is_default_photo = None


class MessagesChatSettingsState:
	"""VK Object MessagesChatSettingsState

	in - None
	kicked - None
	left - None
	"""
	_in = 0
	kicked = 1
	left = 2


class MessagesConversation:
	"""VK Object MessagesConversation

	peer - No description
	sort_id - No description
	last_message_id - ID of the last message in conversation
	in_read - Last message user have read
	out_read - Last outcoming message have been read by the opponent
	unread_count - Unread messages number
	is_marked_unread - Is this conversation uread
	out_read_by - No description
	important - No description
	unanswered - No description
	special_service_type - No description
	message_request_data - No description
	mentions - Ids of messages with mentions
	current_keyboard - No description
	push_settings - No description
	can_write - No description
	chat_settings - No description
	"""
	peer = None
	sort_id = None
	last_message_id = None
	in_read = None
	out_read = None
	unread_count = None
	is_marked_unread = None
	out_read_by = None
	important = None
	unanswered = None
	special_service_type = None
	message_request_data = None
	mentions = None
	current_keyboard = None
	push_settings = None
	can_write = None
	chat_settings = None


class MessagesConversationCanWrite:
	"""VK Object MessagesConversationCanWrite

	allowed - No description
	reason - No description
	"""
	allowed = None
	reason = None


class MessagesConversationMeMber:
	"""VK Object MessagesConversationMeMber

	can_kick - Is it possible for user to kick this member
	invited_by - No description
	is_admin - No description
	is_owner - No description
	is_message_request - No description
	join_date - No description
	request_date - Message request date
	member_id - No description
	"""
	can_kick = None
	invited_by = None
	is_admin = None
	is_owner = None
	is_message_request = None
	join_date = None
	request_date = None
	member_id = None


class MessagesConversationPeer:
	"""VK Object MessagesConversationPeer

	id - No description
	local_id - No description
	type - No description
	"""
	id = None
	local_id = None
	type = None


class MessagesConversationPeerType:
	"""VK Object MessagesConversationPeerType

	chat - None
	email - None
	user - None
	group - None
	"""
	chat = 0
	email = 1
	user = 2
	group = 3


class MessagesConversationSortId:
	"""VK Object MessagesConversationSortId

	major_id - Major id for sorting conversations
	minor_id - Minor id for sorting conversations
	"""
	major_id = None
	minor_id = None


class MessagesConversationWithMessage:
	"""VK Object MessagesConversationWithMessage

	conversation - No description
	last_message - No description
	"""
	conversation = None
	last_message = None


class MessagesForeignMessage:
	"""VK Object MessagesForeignMessage

	attachments - No description
	conversation_message_id - Conversation message ID
	date - Date when the message was created
	from_id - Message author's ID
	fwd_messages - No description
	geo - No description
	id - Message ID
	peer_id - Peer ID
	reply_message - No description
	text - Message text
	update_time - Date when the message has been updated in Unixtime
	was_listened - Was the audio message inside already listened by you
	payload - Additional data sent along with message for developer convenience
	"""
	attachments = None
	conversation_message_id = None
	date = None
	from_id = None
	fwd_messages = None
	geo = None
	id = None
	peer_id = None
	reply_message = None
	text = None
	update_time = None
	was_listened = None
	payload = None


class MessagesForward:
	"""VK Object MessagesForward

	owner_id - Messages owner_id
	peer_id - Messages peer_id
	conversation_message_ids - No description
	message_ids - No description
	is_reply - If you need to reply to a message
	"""
	owner_id = None
	peer_id = None
	conversation_message_ids = None
	message_ids = None
	is_reply = None


class MessagesGraffiti:
	"""VK Object MessagesGraffiti

	access_key - Access key for graffiti
	height - Graffiti height
	id - Graffiti ID
	owner_id - Graffiti owner ID
	url - Graffiti URL
	width - Graffiti width
	"""
	access_key = None
	height = None
	id = None
	owner_id = None
	url = None
	width = None


class MessagesHistoryAttachMent:
	"""VK Object MessagesHistoryAttachMent

	attachment - No description
	message_id - Message ID
	from_id - Message author's ID
	forward_level - Forward level (optional)
	"""
	attachment = None
	message_id = None
	from_id = None
	forward_level = None


class MessagesHistoryMessageAttachMent:
	"""VK Object MessagesHistoryMessageAttachMent

	audio - No description
	audio_message - No description
	doc - No description
	graffiti - No description
	link - No description
	market - No description
	photo - No description
	share - No description
	type - No description
	video - No description
	wall - No description
	"""
	audio = None
	audio_message = None
	doc = None
	graffiti = None
	link = None
	market = None
	photo = None
	share = None
	type = None
	video = None
	wall = None


class MessagesHistoryMessageAttachMentType:
	"""VK Object MessagesHistoryMessageAttachMentType

	photo - None
	video - None
	audio - None
	doc - None
	link - None
	market - None
	wall - None
	share - None
	graffiti - None
	audio_message - None
	"""
	photo = 0
	video = 1
	audio = 2
	doc = 3
	link = 4
	market = 5
	wall = 6
	share = 7
	graffiti = 8
	audio_message = 9


class MessagesKeyboard:
	"""VK Object MessagesKeyboard

	author_id - Community or bot, which set this keyboard
	buttons - No description
	one_time - Should this keyboard disappear on first use
	inline - No description
	"""
	author_id = None
	buttons = None
	one_time = None
	inline = None


class MessagesKeyboardButton:
	"""VK Object MessagesKeyboardButton

	action - No description
	color - Button color
	"""
	action = None
	color = None


class MessagesKeyboardButtonAction:
	"""VK Object MessagesKeyboardButtonAction

	app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
	hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
	label - Label for button
	link - link for button
	owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
	payload - Additional data sent along with message for developer convenience
	type - Button type
	"""
	app_id = None
	hash = None
	label = None
	link = None
	owner_id = None
	payload = None
	type = None


class MessagesLastActivity:
	"""VK Object MessagesLastActivity

	online - Information whether user is online
	time - Time when user was online in Unixtime
	"""
	online = None
	time = None


class MessagesLongpollMessages:
	"""VK Object MessagesLongpollMessages

	count - Total number
	items - No description
	"""
	count = None
	items = None


class MessagesLongpollParaMs:
	"""VK Object MessagesLongpollParaMs

	server - Server URL
	key - Key
	ts - Timestamp
	pts - Persistent timestamp
	"""
	server = None
	key = None
	ts = None
	pts = None


class MessagesMessage:
	"""VK Object MessagesMessage

	action - No description
	admin_author_id - Only for messages from community. Contains user ID of community admin, who sent this message.
	attachments - No description
	conversation_message_id - Unique auto-incremented number for all messages with this peer
	date - Date when the message has been sent in Unixtime
	deleted - Is it an deleted message
	from_id - Message author's ID
	fwd_messages - Forwarded messages
	geo - No description
	id - Message ID
	important - Is it an important message
	is_hidden - No description
	is_cropped - this message is cropped for bot
	keyboard - No description
	members_count - Members number
	out - Information whether the message is outcoming
	payload - No description
	peer_id - Peer ID
	random_id - ID used for sending messages. It returned only for outgoing messages
	ref - No description
	ref_source - No description
	reply_message - No description
	text - Message text
	update_time - Date when the message has been updated in Unixtime
	was_listened - Was the audio message inside already listened by you
	pinned_at - Date when the message has been pinned in Unixtime
	"""
	action = None
	admin_author_id = None
	attachments = None
	conversation_message_id = None
	date = None
	deleted = None
	from_id = None
	fwd_messages = None
	geo = None
	id = None
	important = None
	is_hidden = None
	is_cropped = None
	keyboard = None
	members_count = None
	out = None
	payload = None
	peer_id = None
	random_id = None
	ref = None
	ref_source = None
	reply_message = None
	text = None
	update_time = None
	was_listened = None
	pinned_at = None


class MessagesMessageAction:
	"""VK Object MessagesMessageAction

	conversation_message_id - Message ID
	email - Email address for chat_invite_user or chat_kick_user actions
	member_id - User or email peer ID
	message - Message body of related message
	photo - No description
	text - New chat title for chat_create and chat_title_update actions
	type - No description
	"""
	conversation_message_id = None
	email = None
	member_id = None
	message = None
	photo = None
	text = None
	type = None


class MessagesMessageActionPhoto:
	"""VK Object MessagesMessageActionPhoto

	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	photo_50 - URL of the preview image with 50px in width
	"""
	photo_100 = None
	photo_200 = None
	photo_50 = None


class MessagesMessageActionStatus:
	"""VK Object MessagesMessageActionStatus

	chat_photo_update - None
	chat_photo_remove - None
	chat_create - None
	chat_title_update - None
	chat_invite_user - None
	chat_kick_user - None
	chat_pin_message - None
	chat_unpin_message - None
	chat_invite_user_by_link - None
	"""
	chat_photo_update = 0
	chat_photo_remove = 1
	chat_create = 2
	chat_title_update = 3
	chat_invite_user = 4
	chat_kick_user = 5
	chat_pin_message = 6
	chat_unpin_message = 7
	chat_invite_user_by_link = 8


class MessagesMessageAttachMent:
	"""VK Object MessagesMessageAttachMent

	audio - No description
	audio_message - No description
	call - No description
	doc - No description
	gift - No description
	graffiti - No description
	link - No description
	market - No description
	market_market_album - No description
	photo - No description
	sticker - No description
	story - No description
	type - No description
	video - No description
	wall - No description
	wall_reply - No description
	poll - No description
	"""
	audio = None
	audio_message = None
	call = None
	doc = None
	gift = None
	graffiti = None
	link = None
	market = None
	market_market_album = None
	photo = None
	sticker = None
	story = None
	type = None
	video = None
	wall = None
	wall_reply = None
	poll = None


class MessagesMessageAttachMentType:
	"""VK Object MessagesMessageAttachMentType

	photo - None
	audio - None
	video - None
	doc - None
	link - None
	market - None
	market_album - None
	gift - None
	sticker - None
	wall - None
	wall_reply - None
	article - None
	poll - None
	call - None
	graffiti - None
	audio_message - None
	"""
	photo = 0
	audio = 1
	video = 2
	doc = 3
	link = 4
	market = 5
	market_album = 6
	gift = 7
	sticker = 8
	wall = 9
	wall_reply = 10
	article = 11
	poll = 12
	call = 13
	graffiti = 14
	audio_message = 15


class MessagesMessageRequestData:
	"""VK Object MessagesMessageRequestData

	status - Status of message request
	inviter_id - Message request sender id
	request_date - Message request date
	"""
	status = None
	inviter_id = None
	request_date = None


class MessagesMessagesArray:
	"""VK Object MessagesMessagesArray

	count - No description
	items - No description
	"""
	count = None
	items = None


class MessagesOutReadBy:
	"""VK Object MessagesOutReadBy

	count - No description
	member_ids - No description
	"""
	count = None
	member_ids = None


class MessagesPinnedMessage:
	"""VK Object MessagesPinnedMessage

	attachments - No description
	conversation_message_id - Unique auto-incremented number for all messages with this peer
	date - Date when the message has been sent in Unixtime
	from_id - Message author's ID
	fwd_messages - Forwarded messages
	geo - No description
	id - Message ID
	peer_id - Peer ID
	reply_message - No description
	text - Message text
	keyboard - No description
	"""
	attachments = None
	conversation_message_id = None
	date = None
	from_id = None
	fwd_messages = None
	geo = None
	id = None
	peer_id = None
	reply_message = None
	text = None
	keyboard = None


class MessagesPushSettings:
	"""VK Object MessagesPushSettings

	disabled_forever - Information whether push notifications are disabled forever
	disabled_until - Time until what notifications are disabled
	no_sound - Information whether the sound is on
	"""
	disabled_forever = None
	disabled_until = None
	no_sound = None


class MessagesTeMplateActionTypeNaMes:
	"""VK Object MessagesTeMplateActionTypeNaMes

	text - None
	start - None
	location - None
	vkpay - None
	open_app - None
	open_photo - None
	open_link - None
	callback - None
	"""
	text = 0
	start = 1
	location = 2
	vkpay = 3
	open_app = 4
	open_photo = 5
	open_link = 6
	callback = 7


class MessagesUserXtrInvitedBy:
	"""VK Object MessagesUserXtrInvitedBy

	invited_by - ID of the inviter
	"""
	invited_by = <built-in function iter>


class NewsfeedCommeNtsFilters:
	"""VK Object NewsfeedCommeNtsFilters

	post - None
	photo - None
	video - None
	topic - None
	note - None
	"""
	post = 0
	photo = 1
	video = 2
	topic = 3
	note = 4


class NewsfeedEveNtActivity:
	"""VK Object NewsfeedEveNtActivity

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address = None
	button_text = None
	friends = None
	member_status = None
	text = None
	time = None


class NewsfeedFilters:
	"""VK Object NewsfeedFilters

	post - None
	photo - None
	photo_tag - None
	wall_photo - None
	friend - None
	note - None
	audio - None
	video - None
	audio_playlist - None
	clip - None
	"""
	post = 0
	photo = 1
	photo_tag = 2
	wall_photo = 3
	friend = 4
	note = 5
	audio = 6
	video = 7
	audio_playlist = 8
	clip = 9


class NewsfeedIgNoreItemType:
	"""VK Object NewsfeedIgNoreItemType

	wall - None
	tag - None
	profilephoto - None
	video - None
	photo - None
	audio - None
	"""
	wall = 0
	tag = 1
	profilephoto = 2
	video = 3
	photo = 4
	audio = 5


class NewsfeedItemAudio:
	"""VK Object NewsfeedItemAudio

	audio - No description
	post_id - Post ID
	"""
	audio = <built-in function iter>
	post_id = <built-in function iter>


class NewsfeedItemAudioAudio:
	"""VK Object NewsfeedItemAudioAudio

	count - Audios number
	items - No description
	"""
	count = None
	items = None


class NewsfeedItemBase:
	"""VK Object NewsfeedItemBase

	type - No description
	source_id - Item source ID
	date - Date when item has been added in Unixtime
	"""
	type = None
	source_id = None
	date = None


class NewsfeedItemDigest:
	"""VK Object NewsfeedItemDigest

	feed_id - id of feed in digest
	items - No description
	main_post_ids - No description
	template - type of digest
	header - No description
	footer - No description
	track_code - No description
	"""
	feed_id = <built-in function iter>
	items = <built-in function iter>
	main_post_ids = <built-in function iter>
	template = <built-in function iter>
	header = <built-in function iter>
	footer = <built-in function iter>
	track_code = <built-in function iter>


class NewsfeedItemDigestButtoN:
	"""VK Object NewsfeedItemDigestButtoN

	title - No description
	style - No description
	"""
	title = None
	style = None


class NewsfeedItemDigestFooter:
	"""VK Object NewsfeedItemDigestFooter

	style - No description
	text - text for invite to enable smart feed
	button - No description
	"""
	style = None
	text = None
	button = None


class NewsfeedItemDigestFullItem:
	"""VK Object NewsfeedItemDigestFullItem

	text - No description
	source_name - No description
	attachment_index - No description
	attachment - No description
	style - No description
	post - No description
	"""
	text = None
	source_name = None
	attachment_index = None
	attachment = None
	style = None
	post = None


class NewsfeedItemDigestHeader:
	"""VK Object NewsfeedItemDigestHeader

	title - Title of the header
	subtitle - Subtitle of the header, when title have two strings
	style - No description
	button - No description
	"""
	title = None
	subtitle = None
	style = None
	button = None


class NewsfeedItemDigestItem:
	"""VK Object NewsfeedItemDigestItem

	"""


class NewsfeedItemFrieNd:
	"""VK Object NewsfeedItemFrieNd

	friends - No description
	"""
	friends = <built-in function iter>


class NewsfeedItemFrieNdFrieNds:
	"""VK Object NewsfeedItemFrieNdFrieNds

	count - Number of friends has been added
	items - No description
	"""
	count = None
	items = None


class NewsfeedItemHolidayRecommeNdatioNsBlockHeader:
	"""VK Object NewsfeedItemHolidayRecommeNdatioNsBlockHeader

	title - Title of the header
	subtitle - Subtitle of the header
	image - No description
	action - No description
	"""
	title = None
	subtitle = None
	image = None
	action = None


class NewsfeedItemPhoto:
	"""VK Object NewsfeedItemPhoto

	photos - No description
	post_id - Post ID
	"""
	photos = <built-in function iter>
	post_id = <built-in function iter>


class NewsfeedItemPhotoPhotos:
	"""VK Object NewsfeedItemPhotoPhotos

	count - Photos number
	items - No description
	"""
	count = None
	items = None


class NewsfeedItemPhotoTag:
	"""VK Object NewsfeedItemPhotoTag

	photo_tags - No description
	post_id - Post ID
	"""
	photo_tags = <built-in function iter>
	post_id = <built-in function iter>


class NewsfeedItemPhotoTagPhotoTags:
	"""VK Object NewsfeedItemPhotoTagPhotoTags

	count - Tags number
	items - No description
	"""
	count = None
	items = None


class NewsfeedItemPromoButtoN:
	"""VK Object NewsfeedItemPromoButtoN

	text - No description
	title - No description
	action - No description
	images - No description
	track_code - No description
	"""
	text = <built-in function iter>
	title = <built-in function iter>
	action = <built-in function iter>
	images = <built-in function iter>
	track_code = <built-in function iter>


class NewsfeedItemPromoButtoNActioN:
	"""VK Object NewsfeedItemPromoButtoNActioN

	url - No description
	type - No description
	target - No description
	"""
	url = None
	type = None
	target = None


class NewsfeedItemPromoButtoNImage:
	"""VK Object NewsfeedItemPromoButtoNImage

	width - No description
	height - No description
	url - No description
	"""
	width = None
	height = None
	url = None


class NewsfeedItemTopic:
	"""VK Object NewsfeedItemTopic

	comments - No description
	likes - No description
	post_id - Topic post ID
	text - Post text
	"""
	comments = <built-in function iter>
	likes = <built-in function iter>
	post_id = <built-in function iter>
	text = <built-in function iter>


class NewsfeedItemVideo:
	"""VK Object NewsfeedItemVideo

	video - No description
	"""
	video = <built-in function iter>


class NewsfeedItemVideoVideo:
	"""VK Object NewsfeedItemVideoVideo

	count - Tags number
	items - No description
	"""
	count = None
	items = None


class NewsfeedItemWallpost:
	"""VK Object NewsfeedItemWallpost

	activity - No description
	attachments - No description
	comments - No description
	copy_history - No description
	feedback - No description
	geo - No description
	is_favorite - Information whether the post in favorites list
	likes - No description
	marked_as_ads - Information whether the post is marked as ads
	post_id - Post ID
	post_source - No description
	post_type - No description
	reposts - No description
	signer_id - Post signer ID
	text - Post text
	views - Count of views
	short_text_rate - Preview length control parameter
	"""
	activity = <built-in function iter>
	attachments = <built-in function iter>
	comments = <built-in function iter>
	copy_history = <built-in function iter>
	feedback = <built-in function iter>
	geo = <built-in function iter>
	is_favorite = <built-in function iter>
	likes = <built-in function iter>
	marked_as_ads = <built-in function iter>
	post_id = <built-in function iter>
	post_source = <built-in function iter>
	post_type = <built-in function iter>
	reposts = <built-in function iter>
	signer_id = <built-in function iter>
	text = <built-in function iter>
	views = <built-in function iter>
	short_text_rate = <built-in function iter>


class NewsfeedItemWallpostFeedback:
	"""VK Object NewsfeedItemWallpostFeedback

	type - No description
	question - No description
	answers - No description
	stars_count - No description
	gratitude - No description
	"""
	type = None
	question = None
	answers = None
	stars_count = None
	gratitude = None


class NewsfeedItemWallpostFeedbackANswer:
	"""VK Object NewsfeedItemWallpostFeedbackANswer

	title - No description
	id - No description
	"""
	title = None
	id = None


class NewsfeedItemWallpostFeedbackType:
	"""VK Object NewsfeedItemWallpostFeedbackType

	buttons - None
	stars - None
	"""
	buttons = 0
	stars = 1


class NewsfeedItemWallpostType:
	"""VK Object NewsfeedItemWallpostType

	post - None
	copy - None
	reply - None
	"""
	post = 0
	copy = 1
	reply = 2


class NewsfeedList:
	"""VK Object NewsfeedList

	id - List ID
	title - List title
	"""
	id = None
	title = None


class NewsfeedListFull:
	"""VK Object NewsfeedListFull

	no_reposts - Information whether reposts hiding is enabled
	source_ids - No description
	"""
	no_reposts = <built-in function iter>
	source_ids = <built-in function iter>
None

class NewsfeedNewsfeedItemType:
	"""VK Object NewsfeedNewsfeedItemType

	post - None
	photo - None
	photo_tag - None
	wall_photo - None
	friend - None
	audio - None
	video - None
	topic - None
	digest - None
	stories - None
	"""
	post = 0
	photo = 1
	photo_tag = 2
	wall_photo = 3
	friend = 4
	audio = 5
	video = 6
	topic = 7
	digest = 8
	stories = 9


class NewsfeedNewsfeedPhoto:
	"""VK Object NewsfeedNewsfeedPhoto

	likes - No description
	comments - No description
	can_repost - Information whether current user can repost the photo
	"""
	likes = <built-in function iter>
	comments = <built-in function iter>
	can_repost = <built-in function iter>


class NotesNote:
	"""VK Object NotesNote

	read_comments - No description
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
	read_comments = None
	can_comment = None
	comments = None
	date = None
	id = None
	owner_id = None
	text = None
	text_wiki = None
	title = None
	view_url = None


class NotesNoteCommeNt:
	"""VK Object NotesNoteCommeNt

	date - Date when the comment has beed added in Unixtime
	id - Comment ID
	message - Comment text
	nid - Note ID
	oid - Note ID
	reply_to - ID of replied comment 
	uid - Comment author's ID
	"""
	date = None
	id = None
	message = None
	nid = None
	oid = None
	reply_to = None
	uid = None


class NotificatioNsFeedback:
	"""VK Object NotificatioNsFeedback

	attachments - No description
	from_id - Reply author's ID
	geo - No description
	id - Item ID
	likes - No description
	text - Reply text
	to_id - Wall owner's ID
	"""
	attachments = None
	from_id = None
	geo = None
	id = None
	likes = None
	text = None
	to_id = None


class NotificatioNsNotificatioN:
	"""VK Object NotificatioNsNotificatioN

	date - Date when the event has been occurred
	feedback - No description
	parent - No description
	reply - No description
	type - Notification type
	"""
	date = None
	feedback = None
	parent = None
	reply = None
	type = None


class NotificatioNsNotificatioNItem:
	"""VK Object NotificatioNsNotificatioNItem

	"""


class NotificatioNsNotificatioNPareNt:
	"""VK Object NotificatioNsNotificatioNPareNt

	"""


class NotificatioNsNotificatioNsCommeNt:
	"""VK Object NotificatioNsNotificatioNsCommeNt

	date - Date when the comment has been added in Unixtime
	id - Comment ID
	owner_id - Author ID
	photo - No description
	post - No description
	text - Comment text
	topic - No description
	video - No description
	"""
	date = None
	id = None
	owner_id = None
	photo = None
	post = None
	text = None
	topic = None
	video = None


class NotificatioNsReply:
	"""VK Object NotificatioNsReply

	date - Date when the reply has been created in Unixtime
	id - Reply ID
	text - Reply text
	"""
	date = None
	id = None
	text = None


class NotificatioNsSeNdMessageError:
	"""VK Object NotificatioNsSeNdMessageError

	code - Error code
	description - Error description
	"""
	code = None
	description = None


class NotificatioNsSeNdMessageItem:
	"""VK Object NotificatioNsSeNdMessageItem

	user_id - User ID
	status - Notification status
	error - No description
	"""
	user_id = None
	status = None
	error = None


class OauthErrOr:
	"""VK Object OauthErrOr

	error - Error type
	error_description - Error description
	redirect_uri - URI for validation
	"""
	error = None
	error_description = None
	redirect_uri = None


class OrdersAmOunt:
	"""VK Object OrdersAmOunt

	amounts - No description
	currency - Currency name
	"""
	amounts = None
	currency = None


class OrdersAmOuntItem:
	"""VK Object OrdersAmOuntItem

	amount - Votes amount in user's currency
	description - Amount description
	votes - Votes number
	"""
	amount = None
	description = None
	votes = None


class OrdersOrder:
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
	amount = None
	app_order_id = None
	cancel_transaction_id = None
	date = None
	id = None
	item = None
	receiver_id = None
	status = None
	transaction_id = None
	user_id = None


class OrdersSubscriptiOn:
	"""VK Object OrdersSubscriptiOn

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
	cancel_reason = None
	create_time = None
	id = None
	item_id = None
	next_bill_time = None
	pending_cancel = None
	period = None
	period_start_time = None
	price = None
	status = None
	test_mode = None
	trial_expire_time = None
	update_time = None


class OwnerState:
	"""VK Object OwnerState

	state - No description
	description - wiki text to describe user state
	"""
	state = None
	description = None
None

class PagesWikiPage:
	"""VK Object PagesWikiPage

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
	creator_id = None
	creator_name = None
	editor_id = None
	editor_name = None
	group_id = None
	id = None
	title = None
	views = None
	who_can_edit = None
	who_can_view = None


class PagesWikiPageFull:
	"""VK Object PagesWikiPageFull

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
	created = None
	creator_id = None
	current_user_can_edit = None
	current_user_can_edit_access = None
	edited = None
	editor_id = None
	group_id = None
	html = None
	id = None
	source = None
	title = None
	view_url = None
	views = None
	who_can_edit = None
	who_can_view = None


class PagesWikiPageHistory:
	"""VK Object PagesWikiPageHistory

	id - Version ID
	length - Page size in bytes
	date - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	editor_name - Last editor name
	"""
	id = None
	length = None
	date = None
	editor_id = None
	editor_name = None


class PhotosCommentXtrPid:
	"""VK Object PhotosCommentXtrPid

	attachments - No description
	date - Date when the comment has been added in Unixtime
	from_id - Author ID
	id - Comment ID
	likes - No description
	pid - Photo ID
	reply_to_comment - Replied comment ID
	reply_to_user - Replied user ID
	text - Comment text
	parents_stack - No description
	thread - No description
	"""
	attachments = None
	date = None
	from_id = None
	id = None
	likes = None
	pid = None
	reply_to_comment = None
	reply_to_user = None
	text = None
	parents_stack = None
	thread = None


class PhotosImage:
	"""VK Object PhotosImage

	height - Height of the photo in px.
	type - No description
	url - Photo URL.
	width - Width of the photo in px.
	"""
	height = None
	type = None
	url = None
	width = None


class PhotosImageTyPe:
	"""VK Object PhotosImageTyPe

	s - None
	m - None
	x - None
	l - None
	o - None
	p - None
	q - None
	r - None
	y - None
	z - None
	w - None
	"""
	s = 0
	m = 1
	x = 2
	l = 3
	o = 4
	p = 5
	q = 6
	r = 7
	y = 8
	z = 9
	w = 10


class PhotosPhoto:
	"""VK Object PhotosPhoto

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	images - No description
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_256 - URL of image with 2560 px width
	can_comment - Information whether current user can comment the photo
	place - No description
	post_id - Post ID
	sizes - No description
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	has_tags - Whether photo has attached tag links
	restrictions - No description
	"""
	access_key = None
	album_id = None
	date = None
	height = None
	id = None
	images = None
	lat = None
	long = None
	owner_id = None
	photo_256 = None
	can_comment = None
	place = None
	post_id = None
	sizes = None
	text = None
	user_id = None
	width = None
	has_tags = None
	restrictions = None


class PhotosPhotoAlbum:
	"""VK Object PhotosPhotoAlbum

	created - Date when the album has been created in Unixtime
	description - Photo album description
	id - Photo album ID
	owner_id - Album owner's ID
	size - Photos number
	thumb - No description
	title - Photo album title
	updated - Date when the album has been updated last time in Unixtime
	"""
	created = None
	description = None
	id = None
	owner_id = None
	size = None
	thumb = None
	title = None
	updated = None


class PhotosPhotoAlbumFull:
	"""VK Object PhotosPhotoAlbumFull

	can_upload - Information whether current user can upload photo to the album
	comments_disabled - Information whether album comments are disabled
	created - Date when the album has been created in Unixtime
	description - Photo album description
	id - Photo album ID
	owner_id - Album owner's ID
	size - Photos number
	sizes - No description
	thumb_id - Thumb photo ID
	thumb_is_last - Information whether the album thumb is last photo
	thumb_src - URL of the thumb image
	title - Photo album title
	updated - Date when the album has been updated last time in Unixtime
	upload_by_admins_only - Information whether only community administrators can upload photos
	"""
	can_upload = None
	comments_disabled = None
	created = None
	description = None
	id = None
	owner_id = None
	size = None
	sizes = None
	thumb_id = None
	thumb_is_last = None
	thumb_src = None
	title = None
	updated = None
	upload_by_admins_only = None
None

class PhotosPhotoFull:
	"""VK Object PhotosPhotoFull

	access_key - Access key for the photo
	album_id - Album ID
	can_comment - Information whether current user can comment the photo
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	images - No description
	lat - Latitude
	likes - No description
	reposts - No description
	comments - No description
	long - Longitude
	owner_id - Photo owner's ID
	post_id - Post ID
	tags - No description
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	can_comment = None
	date = None
	height = None
	id = None
	images = None
	lat = None
	likes = None
	reposts = None
	comments = None
	long = None
	owner_id = None
	post_id = None
	tags = None
	text = None
	user_id = None
	width = None


class PhotosPhotoFullXtrRealOffset:
	"""VK Object PhotosPhotoFullXtrRealOffset

	access_key - Access key for the photo
	album_id - Album ID
	can_comment - No description
	comments - No description
	date - Date when uploaded
	height - Original photo height
	hidden - Returns if the photo is hidden above the wall
	id - Photo ID
	lat - Latitude
	likes - No description
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
	reposts - No description
	sizes - No description
	tags - No description
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	can_comment = None
	comments = None
	date = None
	height = None
	hidden = None
	id = None
	lat = None
	likes = None
	long = None
	owner_id = None
	photo_1280 = None
	photo_130 = None
	photo_2560 = None
	photo_604 = None
	photo_75 = None
	photo_807 = None
	post_id = None
	real_offset = None
	reposts = None
	sizes = None
	tags = None
	text = None
	user_id = None
	width = None


class PhotosPhotoSizes:
	"""VK Object PhotosPhotoSizes

	height - Height in px
	url - URL of the image
	src - URL of the image
	type - No description
	width - Width in px
	"""
	height = None
	url = None
	src = None
	type = None
	width = None


class PhotosPhotoSizesTyPe:
	"""VK Object PhotosPhotoSizesTyPe

	s - None
	m - None
	x - None
	o - None
	p - None
	q - None
	r - None
	k - None
	l - None
	y - None
	z - None
	c - None
	w - None
	a - None
	b - None
	e - None
	i - None
	d - None
	j - None
	temp - None
	h - None
	g - None
	n - None
	f - None
	max - None
	"""
	s = 0
	m = 1
	x = 2
	o = 3
	p = 4
	q = 5
	r = 6
	k = 7
	l = 8
	y = 9
	z = 10
	c = 11
	w = 12
	a = 13
	b = 14
	e = 15
	i = 16
	d = 17
	j = 18
	temp = 19
	h = 20
	g = 21
	n = 22
	f = 23
	max = 24


class PhotosPhotoTag:
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
	date = None
	id = None
	placer_id = None
	tagged_name = None
	description = None
	user_id = None
	viewed = None
	x = None
	x2 = None
	y = None
	y2 = None


class PhotosPhotoUPload:
	"""VK Object PhotosPhotoUPload

	album_id - Album ID
	upload_url - URL to upload photo
	fallback_upload_url - Fallback URL if upload_url returned error
	user_id - User ID
	group_id - Group ID
	"""
	album_id = None
	upload_url = None
	fallback_upload_url = None
	user_id = None
	group_id = None


class PhotosPhotoXtrRealOffset:
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
	sizes - No description
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	date = None
	height = None
	hidden = None
	id = None
	lat = None
	long = None
	owner_id = None
	photo_1280 = None
	photo_130 = None
	photo_2560 = None
	photo_604 = None
	photo_75 = None
	photo_807 = None
	post_id = None
	real_offset = None
	sizes = None
	text = None
	user_id = None
	width = None


class PhotosPhotoXtrTagInfo:
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
	sizes - No description
	tag_created - Date when tag has been added in Unixtime
	tag_id - Tag ID
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	date = None
	height = None
	id = None
	lat = None
	long = None
	owner_id = None
	photo_1280 = None
	photo_130 = None
	photo_2560 = None
	photo_604 = None
	photo_75 = None
	photo_807 = None
	placer_id = None
	post_id = None
	sizes = None
	tag_created = None
	tag_id = None
	text = None
	user_id = None
	width = None


class PhotosTagsSuggestionItem:
	"""VK Object PhotosTagsSuggestionItem

	title - No description
	caption - No description
	type - No description
	buttons - No description
	photo - No description
	tags - No description
	track_code - No description
	"""
	title = None
	caption = None
	type = None
	buttons = None
	photo = None
	tags = None
	track_code = None


class PhotosTagsSuggestionItemButton:
	"""VK Object PhotosTagsSuggestionItemButton

	title - No description
	action - No description
	style - No description
	"""
	title = None
	action = None
	style = None


class PodcastCover:
	"""VK Object PodcastCover

	sizes - No description
	"""
	sizes = None


class PodcastExternalData:
	"""VK Object PodcastExternalData

	url - Url of the podcast page
	owner_url - Url of the podcasts owner community
	title - Podcast title
	owner_name - Name of the podcasts owner community
	cover - Podcast cover
	"""
	url = None
	owner_url = None
	title = None
	owner_name = None
	cover = None


class PollsAnswer:
	"""VK Object PollsAnswer

	id - Answer ID
	rate - Answer rate in percents
	text - Answer text
	votes - Votes number
	"""
	id = None
	rate = None
	text = None
	votes = None


class PollsBackground:
	"""VK Object PollsBackground

	angle - Gradient angle with 0 on positive X axis
	color - Hex color code without #
	height - Original height of pattern tile
	id - No description
	name - No description
	images - Pattern tiles
	points - Gradient points
	type - No description
	width - Original with of pattern tile
	"""
	angle = None
	color = None
	height = None
	id = None
	name = None
	images = None
	points = None
	type = None
	width = None


class PollsFriend:
	"""VK Object PollsFriend

	id - No description
	"""
	id = None


class PollsPoll:
	"""VK Object PollsPoll

	anonymous - No description
	friends - No description
	multiple - Information whether the poll with multiple choices
	answer_id - Current user's answer ID
	end_date - No description
	answer_ids - Current user's answer IDs
	closed - No description
	is_board - No description
	can_edit - No description
	can_vote - No description
	can_report - No description
	can_share - No description
	photo - No description
	answers - No description
	created - Date when poll has been created in Unixtime
	id - Poll ID
	owner_id - Poll owner's ID
	author_id - Poll author's ID
	question - Poll question
	background - No description
	votes - Votes number
	disable_unvote - No description
	"""
	anonymous = None
	friends = None
	multiple = None
	answer_id = None
	end_date = None
	answer_ids = None
	closed = None
	is_board = None
	can_edit = None
	can_vote = None
	can_report = None
	can_share = None
	photo = None
	answers = None
	created = None
	id = None
	owner_id = None
	author_id = None
	question = None
	background = None
	votes = None
	disable_unvote = None
None

class PollsVoters:
	"""VK Object PollsVoters

	answer_id - Answer ID
	users - No description
	"""
	answer_id = None
	users = None


class PollsVotersUsers:
	"""VK Object PollsVotersUsers

	count - Votes number
	items - No description
	"""
	count = None
	items = None


class PrettyCardsPrettyCard:
	"""VK Object PrettyCardsPrettyCard

	button - Button key
	button_text - Button text in current language
	card_id - Card ID (long int returned as string)
	images - No description
	link_url - Link URL
	photo - Photo ID (format "<owner_id>_<media_id>")
	price - Price if set (decimal number returned as string)
	price_old - Old price if set (decimal number returned as string)
	title - Title
	"""
	button = None
	button_text = None
	card_id = None
	images = None
	link_url = None
	photo = None
	price = None
	price_old = None
	title = None


class SearchHint:
	"""VK Object SearchHint

	app - No description
	description - Object description
	global - Information whether the object has been found globally
	group - No description
	profile - No description
	section - No description
	type - No description
	"""
	app = None
	description = None
	_global = None
	group = None
	profile = None
	section = None
	type = None


class SearchHintSection:
	"""VK Object SearchHintSection

	groups - None
	events - None
	publics - None
	correspondents - None
	people - None
	friends - None
	mutual_friends - None
	"""
	groups = 0
	events = 1
	publics = 2
	correspondents = 3
	people = 4
	friends = 5
	mutual_friends = 6


class SearchHintType:
	"""VK Object SearchHintType

	group - None
	profile - None
	vk_app - None
	app - None
	html5_game - None
	"""
	group = 0
	profile = 1
	vk_app = 2
	app = 3
	html5_game = 4


class SecureLevel:
	"""VK Object SecureLevel

	level - Level
	uid - User ID
	"""
	level = None
	uid = None


class SecureSmSNotification:
	"""VK Object SecureSmSNotification

	app_id - Application ID
	date - Date when message has been sent in Unixtime
	id - Notification ID
	message - Messsage text
	user_id - User ID
	"""
	app_id = None
	date = None
	id = None
	message = None
	user_id = None


class SecureTokenChecked:
	"""VK Object SecureTokenChecked

	date - Date when access_token has been generated in Unixtime
	expire - Date when access_token will expire in Unixtime
	success - Returns if successfully processed
	user_id - User ID
	"""
	date = None
	expire = None
	success = None
	user_id = None


class SecureTranSaction:
	"""VK Object SecureTranSaction

	date - Transaction date in Unixtime
	id - Transaction ID
	uid_from - From ID
	uid_to - To ID
	votes - Votes number
	"""
	date = None
	id = None
	uid_from = None
	uid_to = None
	votes = None


class StatSActivity:
	"""VK Object StatSActivity

	comments - Comments number
	copies - Reposts number
	hidden - Hidden from news count
	likes - Likes number
	subscribed - New subscribers count
	unsubscribed - Unsubscribed count
	"""
	comments = None
	copies = None
	hidden = None
	likes = None
	subscribed = None
	unsubscribed = None


class StatSCity:
	"""VK Object StatSCity

	count - Visitors number
	name - City name
	value - City ID
	"""
	count = None
	name = None
	value = None


class StatSCountry:
	"""VK Object StatSCountry

	code - Country code
	count - Visitors number
	name - Country name
	value - Country ID
	"""
	code = None
	count = None
	name = None
	value = None


class StatSPeriod:
	"""VK Object StatSPeriod

	activity - No description
	period_from - Unix timestamp
	period_to - Unix timestamp
	reach - No description
	visitors - No description
	"""
	activity = None
	period_from = None
	period_to = None
	reach = None
	visitors = None


class StatSReach:
	"""VK Object StatSReach

	age - No description
	cities - No description
	countries - No description
	mobile_reach - Reach count from mobile devices
	reach - Reach count
	reach_subscribers - Subscribers reach count
	sex - No description
	sex_age - No description
	"""
	age = None
	cities = None
	countries = None
	mobile_reach = None
	reach = None
	reach_subscribers = None
	sex = None
	sex_age = None


class StatSSexAge:
	"""VK Object StatSSexAge

	count - Visitors number
	value - Sex/age value
	reach - No description
	reach_subscribers - No description
	count_subscribers - No description
	"""
	count = None
	value = None
	reach = None
	reach_subscribers = None
	count_subscribers = None


class StatSViewS:
	"""VK Object StatSViewS

	age - No description
	cities - No description
	countries - No description
	mobile_views - Number of views from mobile devices
	sex - No description
	sex_age - No description
	views - Views number
	visitors - Visitors number
	"""
	age = None
	cities = None
	countries = None
	mobile_views = None
	sex = None
	sex_age = None
	views = None
	visitors = None


class StatSWallpoStStat:
	"""VK Object StatSWallpoStStat

	post_id - No description
	hide - Hidings number
	join_group - People have joined the group
	links - Link clickthrough
	reach_subscribers - Subscribers reach
	reach_subscribers_count - No description
	reach_total - Total reach
	reach_total_count - No description
	reach_viral - No description
	reach_ads - No description
	report - Reports number
	to_group - Clickthrough to community
	unsubscribe - Unsubscribed members
	sex_age - No description
	"""
	post_id = None
	hide = None
	join_group = None
	links = None
	reach_subscribers = None
	reach_subscribers_count = None
	reach_total = None
	reach_total_count = None
	reach_viral = None
	reach_ads = None
	report = None
	to_group = None
	unsubscribe = None
	sex_age = None


class StatuSStatuS:
	"""VK Object StatuSStatuS

	text - Status text
	audio - No description
	"""
	text = None
	audio = None


class StickerSImageSet:
	"""VK Object StickerSImageSet

	base_url - Base URL for images in set
	version - Version number to be appended to the image URL
	"""
	base_url = None
	version = None


class StorageValue:
	"""VK Object StorageValue

	key - No description
	value - No description
	"""
	key = None
	value = None


class StoreProduct:
	"""VK Object StoreProduct

	id - Id of the product
	type - Product type
	purchased - Information whether the product is purchased (1 - yes, 0 - no)
	active - Information whether the product is active (1 - yes, 0 - no)
	promoted - Information whether the product is promoted (1 - yes, 0 - no)
	purchase_date - Date (Unix time) when the product was purchased
	title - Title of the product
	stickers - No description
	icon - Array of icon images or icon set object of the product (for stickers product type)
	previews - Array of preview images of the product (for stickers product type)
	has_animation - Information whether the product is an animated sticker pack (for stickers product type)
	subtitle - Subtitle of the product
	"""
	id = None
	type = None
	purchased = None
	active = None
	promoted = None
	purchase_date = None
	title = None
	stickers = None
	icon = None
	previews = None
	has_animation = None
	subtitle = None
None

class StoreStickerSKeyword:
	"""VK Object StoreStickerSKeyword

	words - No description
	user_stickers - No description
	promoted_stickers - No description
	stickers - No description
	"""
	words = None
	user_stickers = None
	promoted_stickers = None
	stickers = None


class StoreStickerSKeywordSticker:
	"""VK Object StoreStickerSKeywordSticker

	pack_id - Pack id
	sticker_id - Sticker id
	"""
	pack_id = None
	sticker_id = None


class StoreStickerSKeywordStickerS:
	"""VK Object StoreStickerSKeywordStickerS

	"""


class StorieSClickableArea:
	"""VK Object StorieSClickableArea

	x - No description
	y - No description
	"""
	x = None
	y = None


class StorieSClickableSticker:
	"""VK Object StorieSClickableSticker

	clickable_area - No description
	id - Clickable sticker ID
	hashtag - No description
	link_object - No description
	mention - No description
	tooltip_text - No description
	owner_id - No description
	story_id - No description
	question - No description
	question_button - No description
	place_id - No description
	market_item - No description
	audio - No description
	audio_start_time - No description
	style - No description
	type - No description
	subtype - No description
	post_owner_id - No description
	post_id - No description
	poll - No description
	color - Color, hex format
	sticker_id - Sticker ID
	sticker_pack_id - Sticker pack ID
	app - No description
	app_context - Additional context for app sticker
	has_new_interactions - Whether current user has unread interaction with this app
	is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
	situational_theme_id - No description
	situational_app_url - No description
	"""
	clickable_area = None
	id = None
	hashtag = None
	link_object = None
	mention = None
	tooltip_text = None
	owner_id = None
	story_id = None
	question = None
	question_button = None
	place_id = None
	market_item = None
	audio = None
	audio_start_time = None
	style = None
	type = None
	subtype = None
	post_owner_id = None
	post_id = None
	poll = None
	color = None
	sticker_id = None
	sticker_pack_id = None
	app = None
	app_context = None
	has_new_interactions = None
	is_broadcast_notify_allowed = None
	situational_theme_id = None
	situational_app_url = None


class StorieSClickableStickerS:
	"""VK Object StorieSClickableStickerS

	clickable_stickers - No description
	original_height - No description
	original_width - No description
	"""
	clickable_stickers = None
	original_height = None
	original_width = None


class StorieSFeedItem:
	"""VK Object StorieSFeedItem

	type - Type of Feed Item
	id - No description
	stories - Author stories
	grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
	app - App, which stories has been grouped (for type app_grouped_stories)
	promo_data - Additional data for promo stories (for type promo_stories)
	birthday_user_id - No description
	"""
	type = None
	id = None
	stories = None
	grouped = None
	app = None
	promo_data = None
	birthday_user_id = None


class StorieSPromoBlock:
	"""VK Object StorieSPromoBlock

	name - Promo story title
	photo_50 - RL of square photo of the story with 50 pixels in width
	photo_100 - RL of square photo of the story with 100 pixels in width
	not_animated - Hide animation for promo story
	"""
	name = None
	photo_50 = None
	photo_100 = None
	not_animated = None


class StorieSReplieS:
	"""VK Object StorieSReplieS

	count - Replies number.
	new - New replies number.
	"""
	count = None
	new = None


class StorieSStatLine:
	"""VK Object StorieSStatLine

	name - No description
	counter - No description
	is_unavailable - No description
	"""
	name = None
	counter = None
	is_unavailable = None


class StorieSStory:
	"""VK Object StorieSStory

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
	link - No description
	owner_id - Story owner's ID.
	parent_story - No description
	parent_story_access_key - Access key for private object.
	parent_story_id - Parent story ID.
	parent_story_owner_id - Parent story owner's ID.
	photo - No description
	replies - Replies counters to current story.
	seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
	type - No description
	clickable_stickers - No description
	video - No description
	views - Views number.
	can_ask - Information whether story has question sticker and current user can send question to the author
	can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
	narratives_count - No description
	first_narrative_title - No description
	birthday_wish_user_id - No description
	can_use_in_narrative - No description
	"""
	access_key = None
	can_comment = None
	can_reply = None
	can_see = None
	can_like = None
	can_share = None
	can_hide = None
	date = None
	expires_at = None
	id = None
	is_deleted = None
	is_expired = None
	link = None
	owner_id = None
	parent_story = None
	parent_story_access_key = None
	parent_story_id = None
	parent_story_owner_id = None
	photo = None
	replies = None
	seen = None
	type = None
	clickable_stickers = None
	video = None
	views = None
	can_ask = None
	can_ask_anonymous = None
	narratives_count = None
	first_narrative_title = None
	birthday_wish_user_id = None
	can_use_in_narrative = None


class StorieSStoryLink:
	"""VK Object StorieSStoryLink

	text - Link text
	url - Link URL
	"""
	text = None
	url = None


class StorieSStoryStatS:
	"""VK Object StorieSStoryStatS

	answer - No description
	bans - No description
	open_link - No description
	replies - No description
	shares - No description
	subscribers - No description
	views - No description
	likes - No description
	"""
	answer = None
	bans = None
	open_link = None
	replies = None
	shares = None
	subscribers = None
	views = None
	likes = None


class StorieSStoryStatSStat:
	"""VK Object StorieSStoryStatSStat

	count - Stat value
	state - No description
	"""
	count = None
	state = None


class StorieSStoryStatSState:
	"""VK Object StorieSStoryStatSState

	on - None
	off - None
	hidden - None
	"""
	on = 0
	off = 1
	hidden = 2


class StorieSStoryType:
	"""VK Object StorieSStoryType

	photo - None
	video - None
	live_active - None
	live_finished - None
	birthday_invite - None
	"""
	photo = 0
	video = 1
	live_active = 2
	live_finished = 3
	birthday_invite = 4


class StorieSUploadLinkText:
	"""VK Object StorieSUploadLinkText

	to_store - None
	vote - None
	more - None
	book - None
	order - None
	enroll - None
	fill - None
	signup - None
	buy - None
	ticket - None
	write - None
	open - None
	learn_more - None
	view - None
	go_to - None
	contact - None
	watch - None
	play - None
	install - None
	read - None
	calendar - None
	"""
	to_store = 0
	vote = 1
	more = 2
	book = 3
	order = 4
	enroll = 5
	fill = 6
	signup = 7
	buy = 8
	ticket = 9
	write = 10
	open = 11
	learn_more = 12
	view = 13
	go_to = 14
	contact = 15
	watch = 16
	play = 17
	install = 18
	read = 19
	calendar = 20


class StorieSViewerSItem:
	"""VK Object StorieSViewerSItem

	is_liked - user has like for this object
	user_id - user id
	user - No description
	"""
	is_liked = None
	user_id = None
	user = None


class UsersCareer:
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
	city_id = None
	city_name = None
	company = None
	country_id = None
	_from = None
	group_id = None
	id = None
	position = None
	until = None


class UsersExports:
	"""VK Object UsersExports

	facebook - No description
	livejournal - No description
	twitter - No description
	"""
	facebook = None
	livejournal = None
	twitter = None


class UsersFields:
	"""VK Object UsersFields

	first_name_nom - None
	first_name_gen - None
	first_name_dat - None
	first_name_acc - None
	first_name_ins - None
	first_name_abl - None
	last_name_nom - None
	last_name_gen - None
	last_name_dat - None
	last_name_acc - None
	last_name_ins - None
	last_name_abl - None
	photo_id - None
	verified - None
	sex - None
	bdate - None
	city - None
	country - None
	home_town - None
	has_photo - None
	photo_50 - None
	photo_100 - None
	photo_200_orig - None
	photo_200 - None
	photo_400 - None
	photo_400_orig - None
	photo_max - None
	photo_max_orig - None
	photo_max_size - None
	online - None
	lists - None
	domain - None
	has_mobile - None
	contacts - None
	site - None
	education - None
	universities - None
	schools - None
	status - None
	last_seen - None
	followers_count - None
	counters - None
	common_count - None
	occupation - None
	nickname - None
	relatives - None
	relation - None
	personal - None
	connections - None
	exports - None
	wall_comments - None
	activities - None
	interests - None
	music - None
	movies - None
	tv - None
	books - None
	games - None
	about - None
	quotes - None
	can_post - None
	can_see_all_posts - None
	can_see_audio - None
	can_write_private_message - None
	can_send_friend_request - None
	is_favorite - None
	is_hidden_from_feed - None
	timezone - None
	screen_name - None
	maiden_name - None
	crop_photo - None
	is_friend - None
	friend_status - None
	career - None
	military - None
	blacklisted - None
	blacklisted_by_me - None
	can_subscribe_posts - None
	descriptions - None
	trending - None
	mutual - None
	friendship_weeks - None
	can_invite_to_chats - None
	stories_archive_count - None
	video_live_level - None
	video_live_count - None
	clips_count - None
	service_description - None
	is_dead - None
	"""
	first_name_nom = 0
	first_name_gen = 1
	first_name_dat = 2
	first_name_acc = 3
	first_name_ins = 4
	first_name_abl = 5
	last_name_nom = 6
	last_name_gen = 7
	last_name_dat = 8
	last_name_acc = 9
	last_name_ins = 10
	last_name_abl = 11
	photo_id = 12
	verified = 13
	sex = 14
	bdate = 15
	city = 16
	country = 17
	home_town = 18
	has_photo = 19
	photo_50 = 20
	photo_100 = 21
	photo_200_orig = 22
	photo_200 = 23
	photo_400 = 24
	photo_400_orig = 25
	photo_max = 26
	photo_max_orig = 27
	photo_max_size = 28
	online = 29
	lists = 30
	domain = 31
	has_mobile = 32
	contacts = 33
	site = 34
	education = 35
	universities = 36
	schools = 37
	status = 38
	last_seen = 39
	followers_count = 40
	counters = 41
	common_count = 42
	occupation = 43
	nickname = 44
	relatives = 45
	relation = 46
	personal = 47
	connections = 48
	exports = 49
	wall_comments = 50
	activities = 51
	interests = 52
	music = 53
	movies = 54
	tv = 55
	books = 56
	games = 57
	about = 58
	quotes = 59
	can_post = 60
	can_see_all_posts = 61
	can_see_audio = 62
	can_write_private_message = 63
	can_send_friend_request = 64
	is_favorite = 65
	is_hidden_from_feed = 66
	timezone = 67
	screen_name = 68
	maiden_name = 69
	crop_photo = 70
	is_friend = 71
	friend_status = 72
	career = 73
	military = 74
	blacklisted = 75
	blacklisted_by_me = 76
	can_subscribe_posts = 77
	descriptions = 78
	trending = 79
	mutual = 80
	friendship_weeks = 81
	can_invite_to_chats = 82
	stories_archive_count = 83
	video_live_level = 84
	video_live_count = 85
	clips_count = 86
	service_description = 87
	is_dead = 88


class UsersLastSeen:
	"""VK Object UsersLastSeen

	platform - Type of the platform that used for the last authorization
	time - Last visit date (in Unix time)
	"""
	platform = None
	time = None


class UsersMilitary:
	"""VK Object UsersMilitary

	country_id - Country ID
	from - From year
	id - Military ID
	unit - Unit name
	unit_id - Unit ID
	until - Till year
	"""
	country_id = None
	_from = None
	id = None
	unit = None
	unit_id = None
	until = None


class UsersOccUpation:
	"""VK Object UsersOccUpation

	id - ID of school, university, company group
	name - Name of occupation
	type - Type of occupation
	"""
	id = None
	name = None
	type = None


class UsersOnlineInfo:
	"""VK Object UsersOnlineInfo

	visible - Whether you can see real online status of user or not
	last_seen - Last time we saw user being active
	is_online - Whether user is currently online or not
	app_id - Application id from which user is currently online or was last seen online
	is_mobile - Is user online from desktop app or mobile app
	status - In case user online is not visible, it indicates approximate timeframe of user online
	"""
	visible = None
	last_seen = None
	is_online = None
	app_id = None
	is_mobile = None
	status = None


class UsersPersonal:
	"""VK Object UsersPersonal

	alcohol - User's views on alcohol
	inspired_by - User's inspired by
	langs - No description
	life_main - User's personal priority in life
	people_main - User's personal priority in people
	political - User's political views
	religion - User's religion
	religion_id - User's religion id
	smoking - User's views on smoking
	"""
	alcohol = None
	inspired_by = None
	langs = None
	life_main = None
	people_main = None
	political = None
	religion = None
	religion_id = None
	smoking = None


class UsersRelative:
	"""VK Object UsersRelative

	birth_date - Date of child birthday (format dd.mm.yyyy)
	id - Relative ID
	name - Name of relative
	type - Relative type
	"""
	birth_date = None
	id = None
	name = None
	type = None


class UsersSchool:
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
	speciality - No description
	"""
	city = None
	_class = None
	country = None
	id = None
	name = None
	type = None
	type_str = None
	year_from = None
	year_graduated = None
	year_to = None
	speciality = None
None

class UsersUniversity:
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
	university_group_id - No description
	"""
	chair = None
	chair_name = None
	city = None
	country = None
	education_form = None
	education_status = None
	faculty = None
	faculty_name = None
	graduation = None
	id = None
	name = None
	university_group_id = None


class UsersUser:
	"""VK Object UsersUser

	sex - User sex
	screen_name - Domain name of the user's page
	photo_50 - URL of square photo of the user with 50 pixels in width
	photo_100 - URL of square photo of the user with 100 pixels in width
	online_info - No description
	online - Information whether the user is online
	online_mobile - Information whether the user is online in mobile site or application
	online_app - Application ID
	verified - Information whether the user is verified
	trending - Information whether the user has a "fire" pictogram.
	friend_status - No description
	mutual - No description
	"""
	sex = <built-in function iter>
	screen_name = <built-in function iter>
	photo_50 = <built-in function iter>
	photo_100 = <built-in function iter>
	online_info = <built-in function iter>
	online = <built-in function iter>
	online_mobile = <built-in function iter>
	online_app = <built-in function iter>
	verified = <built-in function iter>
	trending = <built-in function iter>
	friend_status = <built-in function iter>
	mutual = <built-in function iter>


class UsersUserConnections:
	"""VK Object UsersUserConnections

	skype - User's Skype nickname
	facebook - User's Facebook account
	facebook_name - User's Facebook name
	twitter - User's Twitter account
	livejournal - User's Livejournal account
	instagram - User's Instagram account
	"""
	skype = None
	facebook = None
	facebook_name = None
	twitter = None
	livejournal = None
	instagram = None


class UsersUserCoUnters:
	"""VK Object UsersUserCoUnters

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
	new_photo_tags - No description
	new_recognition_tags - No description
	mutual_friends - No description
	posts - No description
	articles - No description
	wishes - No description
	podcasts - No description
	clips - No description
	clips_followers - No description
	"""
	albums = None
	audios = None
	followers = None
	friends = None
	gifts = None
	groups = None
	notes = None
	online_friends = None
	pages = None
	photos = None
	subscriptions = None
	user_photos = None
	user_videos = None
	videos = None
	new_photo_tags = None
	new_recognition_tags = None
	mutual_friends = None
	posts = None
	articles = None
	wishes = None
	podcasts = None
	clips = None
	clips_followers = None


class UsersUserFUll:
	"""VK Object UsersUserFUll

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
	city - No description
	country - No description
	timezone - User's timezone
	owner_state - No description
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
	type - No description
	email - No description
	skype - No description
	facebook - No description
	facebook_name - No description
	twitter - No description
	livejournal - No description
	instagram - No description
	test - No description
	video_live - No description
	is_video_live_notifications_blocked - No description
	is_service - No description
	service_description - No description
	photo_rec - No description
	photo_medium - No description
	photo_medium_rec - No description
	photo - No description
	photo_big - No description
	photo_400 - No description
	photo_max_size - No description
	language - No description
	stories_archive_count - No description
	wall_default - No description
	can_call - Information whether current user can call
	can_see_wishes - Information whether current user can see the user's wishes
	can_see_gifts - Information whether current user can see the user's gifts
	interests - No description
	books - No description
	tv - No description
	quotes - No description
	about - No description
	games - No description
	movies - No description
	activities - No description
	music - No description
	can_write_private_message - Information whether current user can write private message
	can_send_friend_request - Information whether current user can send a friend request
	can_be_invited_group - Information whether current user can be invited to the community
	mobile_phone - User's mobile phone number
	home_phone - User's additional phone number
	site - User's website
	status_audio - No description
	status - User's status
	activity - User's status
	last_seen - No description
	exports - No description
	crop_photo - No description
	followers_count - Number of user's followers
	video_live_level - User level in live streams achievements
	video_live_count - Number of user's live streams
	clips_count - Number of user's clips
	blacklisted - Information whether current user is in the requested user's blacklist.
	blacklisted_by_me - Information whether the requested user is in current user's blacklist
	is_favorite - Information whether the requested user is in faves of current user
	is_hidden_from_feed - Information whether the requested user is hidden from current user's newsfeed
	common_count - Number of common friends with current user
	occupation - No description
	career - No description
	military - No description
	university - University ID
	university_name - University name
	university_group_id - No description
	faculty - Faculty ID
	faculty_name - Faculty name
	graduation - Graduation year
	education_form - Education form
	education_status - User's education status
	home_town - User hometown
	relation - User relationship status
	relation_partner - No description
	personal - No description
	universities - No description
	schools - No description
	relatives - No description
	is_subscribed_podcasts - Information whether current user is subscribed to podcasts
	can_subscribe_podcasts - Owner in whitelist or not
	can_subscribe_posts - Can subscribe to wall
	counters - No description
	access_key - No description
	can_upload_doc - No description
	hash - No description
	has_email - No description
	"""
	first_name_nom = <built-in function iter>
	first_name_gen = <built-in function iter>
	first_name_dat = <built-in function iter>
	first_name_acc = <built-in function iter>
	first_name_ins = <built-in function iter>
	first_name_abl = <built-in function iter>
	last_name_nom = <built-in function iter>
	last_name_gen = <built-in function iter>
	last_name_dat = <built-in function iter>
	last_name_acc = <built-in function iter>
	last_name_ins = <built-in function iter>
	last_name_abl = <built-in function iter>
	nickname = <built-in function iter>
	maiden_name = <built-in function iter>
	contact_name = <built-in function iter>
	domain = <built-in function iter>
	bdate = <built-in function iter>
	city = <built-in function iter>
	country = <built-in function iter>
	timezone = <built-in function iter>
	owner_state = <built-in function iter>
	photo_200 = <built-in function iter>
	photo_max = <built-in function iter>
	photo_200_orig = <built-in function iter>
	photo_400_orig = <built-in function iter>
	photo_max_orig = <built-in function iter>
	photo_id = <built-in function iter>
	has_photo = <built-in function iter>
	has_mobile = <built-in function iter>
	is_friend = <built-in function iter>
	wall_comments = <built-in function iter>
	can_post = <built-in function iter>
	can_see_all_posts = <built-in function iter>
	can_see_audio = <built-in function iter>
	type = <built-in function iter>
	email = <built-in function iter>
	skype = <built-in function iter>
	facebook = <built-in function iter>
	facebook_name = <built-in function iter>
	twitter = <built-in function iter>
	livejournal = <built-in function iter>
	instagram = <built-in function iter>
	test = <built-in function iter>
	video_live = <built-in function iter>
	is_video_live_notifications_blocked = <built-in function iter>
	is_service = <built-in function iter>
	service_description = <built-in function iter>
	photo_rec = <built-in function iter>
	photo_medium = <built-in function iter>
	photo_medium_rec = <built-in function iter>
	photo = <built-in function iter>
	photo_big = <built-in function iter>
	photo_400 = <built-in function iter>
	photo_max_size = <built-in function iter>
	language = <built-in function iter>
	stories_archive_count = <built-in function iter>
	wall_default = <built-in function iter>
	can_call = <built-in function iter>
	can_see_wishes = <built-in function iter>
	can_see_gifts = <built-in function iter>
	interests = <built-in function iter>
	books = <built-in function iter>
	tv = <built-in function iter>
	quotes = <built-in function iter>
	about = <built-in function iter>
	games = <built-in function iter>
	movies = <built-in function iter>
	activities = <built-in function iter>
	music = <built-in function iter>
	can_write_private_message = <built-in function iter>
	can_send_friend_request = <built-in function iter>
	can_be_invited_group = <built-in function iter>
	mobile_phone = <built-in function iter>
	home_phone = <built-in function iter>
	site = <built-in function iter>
	status_audio = <built-in function iter>
	status = <built-in function iter>
	activity = <built-in function iter>
	last_seen = <built-in function iter>
	exports = <built-in function iter>
	crop_photo = <built-in function iter>
	followers_count = <built-in function iter>
	video_live_level = <built-in function iter>
	video_live_count = <built-in function iter>
	clips_count = <built-in function iter>
	blacklisted = <built-in function iter>
	blacklisted_by_me = <built-in function iter>
	is_favorite = <built-in function iter>
	is_hidden_from_feed = <built-in function iter>
	common_count = <built-in function iter>
	occupation = <built-in function iter>
	career = <built-in function iter>
	military = <built-in function iter>
	university = <built-in function iter>
	university_name = <built-in function iter>
	university_group_id = <built-in function iter>
	faculty = <built-in function iter>
	faculty_name = <built-in function iter>
	graduation = <built-in function iter>
	education_form = <built-in function iter>
	education_status = <built-in function iter>
	home_town = <built-in function iter>
	relation = <built-in function iter>
	relation_partner = <built-in function iter>
	personal = <built-in function iter>
	universities = <built-in function iter>
	schools = <built-in function iter>
	relatives = <built-in function iter>
	is_subscribed_podcasts = <built-in function iter>
	can_subscribe_podcasts = <built-in function iter>
	can_subscribe_posts = <built-in function iter>
	counters = <built-in function iter>
	access_key = <built-in function iter>
	can_upload_doc = <built-in function iter>
	hash = <built-in function iter>
	has_email = <built-in function iter>


class UsersUserMin:
	"""VK Object UsersUserMin

	deactivated - Returns if a profile is deleted or blocked
	first_name - User first name
	hidden - Returns if a profile is hidden.
	id - User ID
	last_name - User last name
	can_access_closed - No description
	is_closed - No description
	"""
	deactivated = None
	first_name = None
	hidden = None
	id = None
	last_name = None
	can_access_closed = None
	is_closed = None
None

class UsersUserSettingsXtr:
	"""VK Object UsersUserSettingsXtr

	connections - No description
	bdate - User's date of birth
	bdate_visibility - Information whether user's birthdate are hidden
	city - No description
	country - No description
	first_name - User first name
	home_town - User's hometown
	last_name - User last name
	maiden_name - User maiden name
	name_request - No description
	personal - No description
	phone - User phone number with some hidden digits
	relation - User relationship status
	relation_partner - No description
	relation_pending - Information whether relation status is pending
	relation_requests - No description
	screen_name - Domain name of the user's page
	sex - User sex
	status - User status
	status_audio - No description
	interests - No description
	languages - No description
	"""
	connections = None
	bdate = None
	bdate_visibility = None
	city = None
	country = None
	first_name = None
	home_town = None
	last_name = None
	maiden_name = None
	name_request = None
	personal = None
	phone = None
	relation = None
	relation_partner = None
	relation_pending = None
	relation_requests = None
	screen_name = None
	sex = None
	status = None
	status_audio = None
	interests = None
	languages = None


class UsersUserType:
	"""VK Object UsersUserType

	profile - None
	"""
	profile = 0


class UsersUserXtrCoUnters:
	"""VK Object UsersUserXtrCoUnters

	"""


class UsersUserXtrType:
	"""VK Object UsersUserXtrType

	type - No description
	"""
	type = <built-in function iter>


class UsersUsersArray:
	"""VK Object UsersUsersArray

	count - Users number
	items - No description
	"""
	count = None
	items = None


class UtilsDomainResolved:
	"""VK Object UtilsDomainResolved

	object_id - Object ID
	group_id - Group ID
	type - No description
	"""
	object_id = None
	group_id = None
	type = None


class UtilsDomainResolvedType:
	"""VK Object UtilsDomainResolvedType

	user - None
	group - None
	application - None
	page - None
	vk_app - None
	community_application - None
	"""
	user = 0
	group = 1
	application = 2
	page = 3
	vk_app = 4
	community_application = 5


class UtilsLastShortenedLink:
	"""VK Object UtilsLastShortenedLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	timestamp - Creation time in Unixtime
	url - Full URL
	views - Total views number
	"""
	access_key = None
	key = None
	short_url = None
	timestamp = None
	url = None
	views = None


class UtilsLinkChecked:
	"""VK Object UtilsLinkChecked

	link - Link URL
	status - No description
	"""
	link = None
	status = None


class UtilsLinkCheckedStatUs:
	"""VK Object UtilsLinkCheckedStatUs

	not_banned - None
	banned - None
	processing - None
	"""
	not_banned = 0
	banned = 1
	processing = 2


class UtilsLinkStats:
	"""VK Object UtilsLinkStats

	key - Link key (characters after vk.cc/)
	stats - No description
	"""
	key = None
	stats = None


class UtilsLinkStatsExtended:
	"""VK Object UtilsLinkStatsExtended

	key - Link key (characters after vk.cc/)
	stats - No description
	"""
	key = None
	stats = None


class UtilsShortLink:
	"""VK Object UtilsShortLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	url - Full URL
	"""
	access_key = None
	key = None
	short_url = None
	url = None


class UtilsStats:
	"""VK Object UtilsStats

	timestamp - Start time
	views - Total views number
	"""
	timestamp = None
	views = None


class UtilsStatsCity:
	"""VK Object UtilsStatsCity

	city_id - City ID
	views - Views number
	"""
	city_id = None
	views = None


class UtilsStatsCoUntry:
	"""VK Object UtilsStatsCoUntry

	country_id - Country ID
	views - Views number
	"""
	country_id = None
	views = None


class UtilsStatsExtended:
	"""VK Object UtilsStatsExtended

	cities - No description
	countries - No description
	sex_age - No description
	timestamp - Start time
	views - Total views number
	"""
	cities = None
	countries = None
	sex_age = None
	timestamp = None
	views = None


class UtilsStatsSexAge:
	"""VK Object UtilsStatsSexAge

	age_range - Age denotation
	female -  Views by female users
	male -  Views by male users
	"""
	age_range = None
	female = None
	male = None


class VideoLiVeInfo:
	"""VK Object VideoLiVeInfo

	enabled - No description
	is_notifications_blocked - No description
	"""
	enabled = None
	is_notifications_blocked = None


class VideoLiVeSettings:
	"""VK Object VideoLiVeSettings

	can_rewind - If user car rewind live or not
	is_endless - If live is endless or not
	max_duration - Max possible time for rewind
	"""
	can_rewind = None
	is_endless = None
	max_duration = None


class VideoRestrictionButton:
	"""VK Object VideoRestrictionButton

	action - No description
	title - No description
	"""
	action = None
	title = None


class VideoSaVeResult:
	"""VK Object VideoSaVeResult

	access_key - Video access key
	description - Video description
	owner_id - Video owner ID
	title - Video title
	upload_url - URL for the video uploading
	video_id - Video ID
	"""
	access_key = None
	description = None
	owner_id = None
	title = None
	upload_url = None
	video_id = None


class VideoVideo:
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
	image - No description
	first_frame - No description
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
	restriction - No description
	added - 1 if video is added to user's albums
	is_subscribed - 1 if user is subscribed to author of the video
	track_code - No description
	repeat - Information whether the video is repeated
	type - No description
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
	likes - No description
	reposts - No description
	"""
	access_key = <built-in function iter>
	adding_date = <built-in function iter>
	can_comment = <built-in function iter>
	can_edit = <built-in function iter>
	can_like = <built-in function iter>
	can_repost = <built-in function iter>
	can_subscribe = <built-in function iter>
	can_add_to_faves = <built-in function iter>
	can_add = <built-in function iter>
	can_attach_link = <built-in function iter>
	is_private = <built-in function iter>
	comments = <built-in function iter>
	date = <built-in function iter>
	description = <built-in function iter>
	duration = <built-in function iter>
	image = <built-in function iter>
	first_frame = <built-in function iter>
	width = <built-in function iter>
	height = <built-in function iter>
	id = <built-in function iter>
	owner_id = <built-in function iter>
	user_id = <built-in function iter>
	title = <built-in function iter>
	is_favorite = <built-in function iter>
	player = <built-in function iter>
	processing = <built-in function iter>
	converting = <built-in function iter>
	restriction = <built-in function iter>
	added = <built-in function iter>
	is_subscribed = <built-in function iter>
	track_code = <built-in function iter>
	repeat = <built-in function iter>
	type = <built-in function iter>
	views = <built-in function iter>
	local_views = <built-in function iter>
	content_restricted = <built-in function iter>
	content_restricted_message = <built-in function iter>
	balance = <built-in function iter>
	live_status = <built-in function iter>
	live = <built-in function iter>
	upcoming = <built-in function iter>
	live_start_time = <built-in function iter>
	live_notify = <built-in function iter>
	spectators = <built-in function iter>
	platform = <built-in function iter>
	likes = <built-in function iter>
	reposts = <built-in function iter>


class VideoVideoAlbumFull:
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
	count = None
	id = None
	image = None
	image_blur = None
	is_system = None
	owner_id = None
	title = None
	updated_time = None


class VideoVideoFiles:
	"""VK Object VideoVideoFiles

	external - URL of the external player
	mp4_240 - URL of the mpeg4 file with 240p quality
	mp4_360 - URL of the mpeg4 file with 360p quality
	mp4_480 - URL of the mpeg4 file with 480p quality
	mp4_720 - URL of the mpeg4 file with 720p quality
	mp4_1080 - URL of the mpeg4 file with 1080p quality
	flv_320 - URL of the flv file with 320p quality
	"""
	external = None
	mp4_240 = None
	mp4_360 = None
	mp4_480 = None
	mp4_720 = None
	mp4_1080 = None
	flv_320 = None


class VideoVideoFull:
	"""VK Object VideoVideoFull

	files - No description
	live_settings - Settings for live stream
	"""
	files = <built-in function iter>
	live_settings = <built-in function iter>


class VideoVideoImage:
	"""VK Object VideoVideoImage

	with_padding - No description
	"""
	with_padding = <built-in function iter>


class WallAppPost:
	"""VK Object WallAppPost

	id - Application ID
	name - Application name
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id = None
	name = None
	photo_130 = None
	photo_604 = None


class WallAttachedNote:
	"""VK Object WallAttachedNote

	comments - Comments number
	date - Date when the note has been created in Unixtime
	id - Note ID
	owner_id - Note owner's ID
	read_comments - Read comments number
	title - Note title
	view_url - URL of the page with note preview
	"""
	comments = None
	date = None
	id = None
	owner_id = None
	read_comments = None
	title = None
	view_url = None


class WallCarouselBase:
	"""VK Object WallCarouselBase

	carousel_offset - Index of current carousel element
	"""
	carousel_offset = None


class WallCommentAttachment:
	"""VK Object WallCommentAttachment

	audio - No description
	doc - No description
	link - No description
	market - No description
	market_market_album - No description
	note - No description
	page - No description
	photo - No description
	sticker - No description
	type - No description
	video - No description
	"""
	audio = None
	doc = None
	link = None
	market = None
	market_market_album = None
	note = None
	page = None
	photo = None
	sticker = None
	type = None
	video = None


class WallCommentAttachmentType:
	"""VK Object WallCommentAttachmentType

	photo - None
	audio - None
	video - None
	doc - None
	link - None
	note - None
	page - None
	market_market_album - None
	market - None
	sticker - None
	"""
	photo = 0
	audio = 1
	video = 2
	doc = 3
	link = 4
	note = 5
	page = 6
	market_market_album = 7
	market = 8
	sticker = 9


class WallGeo:
	"""VK Object WallGeo

	coordinates - Coordinates as string. <latitude> <longtitude>
	place - No description
	showmap - Information whether a map is showed
	type - Place type
	"""
	coordinates = None
	place = None
	showmap = None
	type = None


class WallGraffiti:
	"""VK Object WallGraffiti

	id - Graffiti ID
	owner_id - Graffiti owner's ID
	photo_200 - URL of the preview image with 200 px in width
	photo_586 - URL of the preview image with 586 px in width
	"""
	id = None
	owner_id = None
	photo_200 = None
	photo_586 = None


class WallPostCopyright:
	"""VK Object WallPostCopyright

	id - No description
	link - No description
	name - No description
	type - No description
	"""
	id = None
	link = None
	name = None
	type = None


class WallPostSource:
	"""VK Object WallPostSource

	data - Additional data
	platform - Platform name
	type - No description
	url - URL to an external site used to publish the post
	"""
	data = None
	platform = None
	type = None
	url = None


class WallPostSourceType:
	"""VK Object WallPostSourceType

	vk - None
	widget - None
	api - None
	rss - None
	sms - None
	mvk - None
	"""
	vk = 0
	widget = 1
	api = 2
	rss = 3
	sms = 4
	mvk = 5


class WallPostType:
	"""VK Object WallPostType

	post - None
	copy - None
	reply - None
	postpone - None
	suggest - None
	"""
	post = 0
	copy = 1
	reply = 2
	postpone = 3
	suggest = 4


class WallPostedPhoto:
	"""VK Object WallPostedPhoto

	id - Photo ID
	owner_id - Photo owner's ID
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id = None
	owner_id = None
	photo_130 = None
	photo_604 = None


class WallVieWs:
	"""VK Object WallVieWs

	count - Count
	"""
	count = None


class WallWallComment:
	"""VK Object WallWallComment

	attachments - No description
	date - Date when the comment has been added in Unixtime
	donut - No description
	from_id - Author ID
	id - Comment ID
	likes - No description
	real_offset - Real position of the comment
	reply_to_comment - Replied comment ID
	reply_to_user - Replied user ID
	text - Comment text
	thread - No description
	post_id - No description
	owner_id - No description
	parents_stack - No description
	deleted - No description
	"""
	attachments = None
	date = None
	donut = None
	from_id = None
	id = None
	likes = None
	real_offset = None
	reply_to_comment = None
	reply_to_user = None
	text = None
	thread = None
	post_id = None
	owner_id = None
	parents_stack = None
	deleted = None


class WallWallCommentDonut:
	"""VK Object WallWallCommentDonut

	is_don - Means commentator is donator
	placeholder - No description
	"""
	is_don = None
	placeholder = None


class WallWallCommentDonutPlaceholder:
	"""VK Object WallWallCommentDonutPlaceholder

	text - No description
	"""
	text = None


class WallWallpost:
	"""VK Object WallWallpost

	access_key - Access key to private object
	attachments - No description
	copyright - Information about the source of the post
	date - Date of publishing in Unixtime
	edited - Date of editing in Unixtime
	from_id - Post author ID
	geo - No description
	id - Post ID
	is_archived - Is post archived, only for post owners
	is_favorite - Information whether the post in favorites list
	likes - Count of likes
	owner_id - Wall owner's ID
	poster - No description
	post_id - If post type 'reply', contains original post ID
	parents_stack - If post type 'reply', contains original parent IDs stack
	post_source - No description
	post_type - No description
	reposts - No description
	signer_id - Post signer ID
	text - Post text
	views - Count of views
	"""
	access_key = None
	attachments = None
	copyright = None
	date = None
	edited = None
	from_id = None
	geo = None
	id = None
	is_archived = None
	is_favorite = None
	likes = None
	owner_id = None
	poster = None
	post_id = None
	parents_stack = None
	post_source = None
	post_type = None
	reposts = None
	signer_id = None
	text = None
	views = None


class WallWallpostAttachment:
	"""VK Object WallWallpostAttachment

	access_key - Access key for the audio
	album - No description
	app - No description
	audio - No description
	doc - No description
	event - No description
	group - No description
	graffiti - No description
	link - No description
	market - No description
	market_album - No description
	note - No description
	page - No description
	photo - No description
	photos_list - No description
	poll - No description
	posted_photo - No description
	type - No description
	video - No description
	"""
	access_key = None
	album = None
	app = None
	audio = None
	doc = None
	event = None
	group = None
	graffiti = None
	link = None
	market = None
	market_album = None
	note = None
	page = None
	photo = None
	photos_list = None
	poll = None
	posted_photo = None
	type = None
	video = None


class WallWallpostAttachmentType:
	"""VK Object WallWallpostAttachmentType

	photo - None
	posted_photo - None
	audio - None
	video - None
	doc - None
	link - None
	graffiti - None
	note - None
	app - None
	poll - None
	page - None
	album - None
	photos_list - None
	market_market_album - None
	market - None
	event - None
	"""
	photo = 0
	posted_photo = 1
	audio = 2
	video = 3
	doc = 4
	link = 5
	graffiti = 6
	note = 7
	app = 8
	poll = 9
	page = 10
	album = 11
	photos_list = 12
	market_market_album = 13
	market = 14
	event = 15


class WallWallpostCommentsDonut:
	"""VK Object WallWallpostCommentsDonut

	placeholder - No description
	"""
	placeholder = None


class WallWallpostCommentsDonutPlaceholder:
	"""VK Object WallWallpostCommentsDonutPlaceholder

	text - No description
	"""
	text = None


class WallWallpostDonut:
	"""VK Object WallWallpostDonut

	is_donut - Post only for dons
	paid_duration - Value of this field need to pass in wall.post/edit in donut_paid_duration
	placeholder - If placeholder was respond, text and all attachments will be hidden
	can_publish_free_copy - Says whether group admin can post free copy of this donut post
	edit_mode - Says what user can edit in post about donut properties
	"""
	is_donut = None
	paid_duration = None
	placeholder = None
	can_publish_free_copy = None
	edit_mode = None


class WallWallpostDonutPlaceholder:
	"""VK Object WallWallpostDonutPlaceholder

	text - No description
	"""
	text = None


class WallWallpostFull:
	"""VK Object WallWallpostFull

	copy_history - No description
	can_edit - Information whether current user can edit the post
	created_by - Post creator ID (if post still can be edited)
	can_delete - Information whether current user can delete the post
	can_pin - Information whether current user can pin the post
	donut - No description
	is_pinned - Information whether the post is pinned
	comments - No description
	marked_as_ads - Information whether the post is marked as ads
	short_text_rate - Preview length control parameter
	"""
	copy_history = <built-in function iter>
	can_edit = <built-in function iter>
	created_by = <built-in function iter>
	can_delete = <built-in function iter>
	can_pin = <built-in function iter>
	donut = <built-in function iter>
	is_pinned = <built-in function iter>
	comments = <built-in function iter>
	marked_as_ads = <built-in function iter>
	short_text_rate = <built-in function iter>


class WallWallpostToId:
	"""VK Object WallWallpostToId

	attachments - No description
	comments - No description
	copy_owner_id - ID of the source post owner
	copy_post_id - ID of the source post
	date - Date of publishing in Unixtime
	from_id - Post author ID
	geo - No description
	id - Post ID
	is_favorite - Information whether the post in favorites list
	likes - No description
	post_id - wall post ID (if comment)
	post_source - No description
	post_type - No description
	reposts - No description
	signer_id - Post signer ID
	text - Post text
	to_id - Wall owner's ID
	"""
	attachments = None
	comments = None
	copy_owner_id = None
	copy_post_id = None
	date = None
	from_id = None
	geo = None
	id = None
	is_favorite = None
	likes = None
	post_id = None
	post_source = None
	post_type = None
	reposts = None
	signer_id = None
	text = None
	to_id = None


class WidgetsCommentMedia:
	"""VK Object WidgetsCommentMedia

	item_id - Media item ID
	owner_id - Media owner's ID
	thumb_src - URL of the preview image (type=photo only)
	type - No description
	"""
	item_id = None
	owner_id = None
	thumb_src = None
	type = None


class WidgetsCommentMediaType:
	"""VK Object WidgetsCommentMediaType

	audio - None
	photo - None
	video - None
	"""
	audio = 0
	photo = 1
	video = 2


class WidgetsCommentReplies:
	"""VK Object WidgetsCommentReplies

	can_post - Information whether current user can comment the post
	count - Comments number
	replies - No description
	"""
	can_post = None
	count = None
	replies = None


class WidgetsCommentRepliesItem:
	"""VK Object WidgetsCommentRepliesItem

	cid - Comment ID
	date - Date when the comment has been added in Unixtime
	likes - No description
	text - Comment text
	uid - User ID
	user - No description
	"""
	cid = None
	date = None
	likes = None
	text = None
	uid = None
	user = None


class WidgetsWidgetComment:
	"""VK Object WidgetsWidgetComment

	attachments - No description
	can_delete - Information whether current user can delete the comment
	comments - No description
	date - Date when the comment has been added in Unixtime
	from_id - Comment author ID
	id - Comment ID
	likes - No description
	media - No description
	post_source - No description
	post_type - Post type
	reposts - No description
	text - Comment text
	to_id - Wall owner
	user - No description
	"""
	attachments = None
	can_delete = None
	comments = None
	date = None
	from_id = None
	id = None
	likes = None
	media = None
	post_source = None
	post_type = None
	reposts = None
	text = None
	to_id = None
	user = None


class WidgetsWidgetLikes:
	"""VK Object WidgetsWidgetLikes

	count - Likes number
	"""
	count = None


class WidgetsWidgetPage:
	"""VK Object WidgetsWidgetPage

	comments - No description
	date - Date when widgets on the page has been initialized firstly in Unixtime
	description - Page description
	id - Page ID
	likes - No description
	page_id - page_id parameter value
	photo - URL of the preview image
	title - Page title
	url - Page absolute URL
	"""
	comments = None
	date = None
	description = None
	id = None
	likes = None
	page_id = None
	photo = None
	title = None
	url = None
