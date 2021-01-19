using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void ReadWinners(List<string> winnersList, string fileName)
        {
            // open winners list txt file

            
        }

        private void listBoxTeams_SelectedIndexChanged(object sender, EventArgs e)
        {
            
            
            
        }

        private void buttonLoad_Click(object sender, EventArgs e)
        {
            int counter = 0;
            string line;

            // read file and display it line by line
            System.IO.StreamReader file = new System.IO.StreamReader(@"C:\Users\isaia\OneDrive\Documents\C#\Midterm\Teams.txt");

            while ((line = file.ReadLine()) != null)
            {
                listBoxTeams.Items.Insert(counter, line);

                // increase index
                counter++;
            }

            file.Close(); // close the file
        }

        private void buttonCheck_Click(object sender, EventArgs e)
        {
            var winners = File.ReadAllLines(@"C:\Users\isaia\OneDrive\Documents\C#\Midterm\WorldSeriesWinners.txt");
            var team = listBoxTeams.SelectedItem.ToString();
            var count = 0;
            for(var i = 0; i < winners.Length; i++)
            {
                if (winners[i].Contains(team)) count++;
            }

            string title = "Winners or Losers?";
            string message = listBoxTeams.SelectedItem.ToString() + " won the world series" +
                " " + count + " time(s)";
            MessageBox.Show(message, title);
        }

        
    }
}
