# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Invoice does not apply",
    "summary": "Basis for not applying invoice to sales orde",
    "author": "Xetechs, S.A.",
    "website": "https://www.xetechs.com",
    "support": "Esdras Santos -> esantos@xetechs.com",
    "category": "Invoice Status",
    "version": "1.1",
    "license": "AGPL-3",
    "external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    "depends": ["sale", "account"],
    "data": ["views/nothing_toinvoice_view.xml"],
    "installable": True,
}
