

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
