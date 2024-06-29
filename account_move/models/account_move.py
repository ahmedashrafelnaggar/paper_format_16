from odoo import models,fields,api
import json



class AccountMove(models.Model):
    _inherit = 'account.move'

    tax_totals_json = fields.Char(string='Tax Totals JSON')



    def prepare_template_data(self):
        data = {
            't-inner-content': '',
            # Other key-value pairs for the template
        }
        return data

    # def render_invoice_template(self, report_invoice):
    #     try:
    #         template = self.env.ref(report_invoice)
    #         rendered_template = template.render_template(report_invoice, {'move': self})
    #         return rendered_template
    #     except Exception as e:
    #         raise ValueError(f"Error rendering template: {e}")
    # @api.model
    # def create(self, values):
    #     if 'tax_totals_json' in values:
    #         values['tax_totals_json'] = json.dumps(self._convert_bool_to_str(values['tax_totals_json']))
    #     return super(AccountMove, self).create(values)

    #
    # @api.depends('tax_totals_json')
    # def _compute_tax_totals(self):
    #     for move in self:
    #         if move.tax_totals_json:
    #             tax_totals = json.loads(move.tax_totals_json)




class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # this field i want to add this field in add line in notebok in model account.move.line
    line_number = fields.Integer(string="Line Number", default=1)
    tax_totals_json = fields.Text(string='Tax Totals JSON')


