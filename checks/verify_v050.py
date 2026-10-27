from pathlib import Path
import hashlib, json, re
r = Path(__file__).resolve().parents[1]
b = (r / "TRACE-v0.5.md").read_bytes()
assert hashlib.sha256(b).hexdigest() == '83d96d5e44b269418a7a772ec2ec79151f8bcb1420ac0b99f90276b289b596a5'
s = b.decode("utf-8")
assert "**Edition:** 0.5.0" in s and "RELEASED RESEARCH SPECIFICATION" in s
blocks = re.findall(r"```json\n(.*?)\n```", s, re.S)
assert [hashlib.sha256(x.encode()).hexdigest() for x in blocks] == ['f5c2d056fb2db353bd659228db03a08ca7d6f151c8d931283203c8dbbe193f14', 'e782f937a9d0fab3de07713d121f35be78736508c1d317ed4aeaa756b0d43826', 'b370378ae07e8e85998e8144d643cebad8e21959d395d336138492f9119b1477', 'ab470d7e07d39e70e4e4268b3357d3301b89746fbcb043b317044de216688193']
for x in blocks: json.loads(x)
assert "efficacy UNVALIDATED" in s and "NOT SHIPPED" in s and "PROPOSED" in s
assert "**Current release:" in (r / "README.md").read_text()
for name, expected in {'TRACE-SPINE.md': 'add22409dcc25d09b26559c7d824ddae047262ac5918a509c2a4234bdc27ce6d', 'TRACE.md': 'b9431ecc07e711c4abd1e70d4159acfd1cb8cecb8bdbd22086e8073b10c01d34', 'AI_TRAINING_PERMISSION.md': 'd4be8ebfecfc5bc2d9b62a92a42df7aa3d78b9a83f3ac0c070c86c05be5371fb'}.items():
    assert hashlib.sha256((r / name).read_bytes()).hexdigest() == expected, name
receipt = json.loads((r / "checks/trace05-v0.5.0.json").read_text())
assert receipt["candidate"]["sha256"] == hashlib.sha256(b).hexdigest()
assert receipt["candidate"]["bytes"] == len(b)
print("v0.5 source, four preserved JSON blocks, donor identities and claim ceilings PASS")
