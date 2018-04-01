from datadog import initialize, api
import settings


# API_KEYとAPP_KEYを指定する。
options = {
    'api_key': settings.API_KEY,
    'app_key': settings.APP_KEY,
}

# datadogのクライアントを初期化する。
initialize(**options)

# ダッシュボードリストの一覧を取得する。
result = api.DashboardList.get_all()
dashboard_lists = result.get('dashboard_lists')

print("ダッシュボードリスト一覧の取得")
print(dashboard_lists)

# ダッシュボートリストの一覧から特定のダッシュボードリストを取得する。
print("ダッシュボードのリスト")
list_ids = []
for dashboard_list in dashboard_lists:
    print(dashboard_list)
    list_ids.append(dashboard_list.get('id'))

print(list_ids)

# ダッシュボードの中身を取得
print("個別のダッシュボードの情報")
for list_id in list_ids:
    dashboard_list = api.DashboardList.get(list_id)
    print(dashboard_list)

# スクリーンボード一覧の取得
print("スクリーンボード一覧の取得")
result = api.Screenboard.get_all()
screenboards = result.get('screenboards')
print(screenboards)


# 個別のスクリーンボードの取得
print("個別のスクリーンボードの取得")
for sb in screenboards:
    print(sb)
    print(sb.get('id'))

    screenboard = api.Screenboard.get(sb.get('id'))
    print("#screenboardの定義情報")
    print(screenboard)




