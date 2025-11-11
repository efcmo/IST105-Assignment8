from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dhcp_dashboard import mongo_connector  # 👈 add this import

@csrf_exempt
def index(request):
    print("✅ POST detected") if request.method == "POST" else None
    db = getattr(mongo_connector, "db", None)  # 👈 get db directly

    if request.method == "POST":
        mac = request.POST.get("mac")
        dhcp = request.POST.get("dhcp")
        print(f"Received MAC: {mac}, DHCP: {dhcp}")

        if db is not None:
            try:
                leases = db.leases
                leases.insert_one({"mac": mac, "dhcp": dhcp})
                print("✅ Insert successful")
            except Exception as e:
                print("❌ Insert failed:", e)
        else:
            print("❌ DB object not found")

    leases_data = []
    if db is not None:
        try:
            leases_data = list(db.leases.find({}, {"_id": 0}))
            print(f"📊 Found {len(leases_data)} leases in MongoDB")
        except Exception as e:
            print("❌ Failed to read from DB:", e)

    return render(request, "index.html", {"leases": leases_data})

