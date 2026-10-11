# Third-party notices

This repository **includes adapted upstream content**, not merely links to it.
Code and skill instructions are MIT licensed; preserve the copyright notices in
[LICENSE](LICENSE) and the complete upstream licenses in `licenses/`.

| Upstream | Included material | License |
| --- | --- | --- |
| [Boom-Vitt/claude-thai-skills](https://github.com/Boom-Vitt/claude-thai-skills/tree/62929a2092e193a64676170a58b8286eaf41c4bc) | Twelve domain skills, utilities, templates and tests, subsequently modified | MIT; see licenses/claude-thai-skills.txt |
| [chakrit/kien-thai](https://github.com/chakrit/kien-thai/tree/3695c889a23538e97ddae45c53e8b894730b41f5) | Thai writing and review guidance, adapted into thai-language and advanced references | MIT; see licenses/kien-thai.txt |

`sources.json` records the exact reviewed commits. The integration adds Thai-input
comprehension and portable installation. External corpora, private assets, native
model routing and upstream runtime hooks are not included.

## Province data

The upstream notice reports that `skills/thai-address/provinces.json` was compiled
using Thailand Post and Wikipedia (CC BY-SA 4.0). The data is therefore excluded
from this repository's blanket MIT statement. See
[DATA_SOURCES.md](skills/thai-address/DATA_SOURCES.md) for attribution, limitations
and the retained share-alike notice.

## External references

Skills reference PyThaiNLP (Apache-2.0), Python Unicode documentation, the optional
`regex` package, and dtinth/promptpay-qr (MIT). These dependencies are not vendored.
Their own licenses apply if installed. Development-only npm dependencies and their
versions are recorded in package-lock.json.

Government and payment references include Revenue Department, PDPC, DOPA, ITMX
and Thailand Post. Linking to public documents does not establish a blanket
public-domain license or official endorsement. Consult the original sources and
current notices. No private service, credential or organization-owned dataset is
required by this package.

For missing or inaccurate attribution, open an issue or pull request with the
relevant source and correction.
